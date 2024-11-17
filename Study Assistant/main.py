# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 23:24:00 2024

@author: ameta
"""

import cv2
import RPi.GPIO as GPIO
import time
import pandas as pd
from datetime import datetime

# GPIO Pin Configuration
WATER_REMINDER_PIN = 17
POSTURE_ALERT_PIN = 27
LCD_PIN_RS = 7
LCD_PIN_E = 8
LCD_PINS_DB = [25, 24, 23, 18]
BUTTON_PIN = 22

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WATER_REMINDER_PIN, GPIO.OUT)
GPIO.setup(POSTURE_ALERT_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Constants
BREAK_INTERVAL = 3600  # 1 hour
WATER_INTERVAL = 1800  # 30 minutes

# Initialize LCD (assuming HD44780-compatible library is used)
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)  # Update with your LCD's I2C address

# Face and Eye Detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize session data logging
session_data = []

# Start session timer
session_start = datetime.now()

def detect_face_and_eyes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        return len(eyes) > 0  # True if eyes are detected
    return False

def log_session_data(start_time, duration, awake):
    session_data.append({
        'Start Time': start_time,
        'Duration (min)': duration,
        'Awake': 'Yes' if awake else 'No'
    })

def display_lcd_message(message):
    lcd.clear()
    lcd.write_string(message)

try:
    cap = cv2.VideoCapture(0)
    last_water_reminder = time.time()
    last_break_reminder = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera not accessible!")
            break

        awake = detect_face_and_eyes(frame)
        cv2.imshow("Study Assistant", frame)

        # Water break reminder
        if time.time() - last_water_reminder > WATER_INTERVAL:
            GPIO.output(WATER_REMINDER_PIN, GPIO.HIGH)
            display_lcd_message("Time for a water break!")
            time.sleep(5)
            GPIO.output(WATER_REMINDER_PIN, GPIO.LOW)
            last_water_reminder = time.time()

        # Sedentary break reminder
        if time.time() - last_break_reminder > BREAK_INTERVAL:
            GPIO.output(POSTURE_ALERT_PIN, GPIO.HIGH)
            display_lcd_message("Time for a break!")
            time.sleep(5)
            GPIO.output(POSTURE_ALERT_PIN, GPIO.LOW)
            last_break_reminder = time.time()

        # Button to stop session
        if not GPIO.input(BUTTON_PIN):
            session_end = datetime.now()
            duration = (session_end - session_start).seconds / 60
            log_session_data(session_start.strftime('%Y-%m-%d %H:%M:%S'), duration, awake)
            print("Session ended.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Save session data to Excel
    df = pd.DataFrame(session_data)
    df.to_excel("session_data.xlsx", index=False)
    print("Session data saved to session_data.xlsx.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    lcd.clear()
