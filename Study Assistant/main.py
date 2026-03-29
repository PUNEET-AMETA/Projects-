import cv2
import RPi.GPIO as GPIO
import time
import pandas as pd
from datetime import datetime
from RPLCD.i2c import CharLCD
import os


WATER_REMINDER_PIN = 17
POSTURE_ALERT_PIN = 27
BUTTON_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(WATER_REMINDER_PIN, GPIO.OUT)
GPIO.setup(POSTURE_ALERT_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


lcd = CharLCD('PCF8574', 0x27)  


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


BREAK_INTERVAL = 3600  
WATER_INTERVAL = 1800  


session_data = []
session_start = datetime.now()
alert_count = 0
water_count = 0


def detect_face_eyes_posture(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))
    eyes_open = False
    bad_posture = False

    for (x, y, w, h) in faces:
        face_center_y = y + h // 2
        frame_center_y = frame.shape[0] // 2

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 1:
            eyes_open = True

        if face_center_y > frame_center_y + 50:
            bad_posture = True
            cv2.putText(frame, "Bad Posture!", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    return eyes_open, bad_posture

def display_lcd_message(message):
    lcd.clear()
    lcd.write_string(message)

def handle_posture_alert():
    global alert_count
    GPIO.output(POSTURE_ALERT_PIN, GPIO.HIGH)
    display_lcd_message("Correct your posture!")
    time.sleep(3)
    GPIO.output(POSTURE_ALERT_PIN, GPIO.LOW)
    alert_count += 1

def handle_water_reminder():
    global water_count
    GPIO.output(WATER_REMINDER_PIN, GPIO.HIGH)
    display_lcd_message("Drink water!")
    time.sleep(5)
    GPIO.output(WATER_REMINDER_PIN, GPIO.LOW)
    water_count += 1

def log_session_data(start_time, duration, awake, posture_ok, alerts, waters):
    session_data.append({
        'Start Time': start_time,
        'Duration (min)': duration,
        'Awake': 'Yes' if awake else 'No',
        'Good Posture': 'Yes' if posture_ok else 'No',
        'Posture Alerts': alerts,
        'Water Reminders': waters
    })


try:
    cap = cv2.VideoCapture(0)
    last_water_reminder = time.time()
    last_break_reminder = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera not accessible!")
            break

        eyes_open, bad_posture = detect_face_eyes_posture(frame)
        cv2.imshow("Study Assistant", frame)

        if bad_posture:
            handle_posture_alert()


        if time.time() - last_water_reminder > WATER_INTERVAL:
            handle_water_reminder()
            last_water_reminder = time.time()


        if time.time() - last_break_reminder > BREAK_INTERVAL:
            display_lcd_message("Take a break!")
            time.sleep(5)
            last_break_reminder = time.time()

       
        if int(time.time()) % 60 == 0:
            elapsed = int(time.time() - session_start.timestamp()) // 60
            display_lcd_message(f"Time: {elapsed} min")

        
        if not GPIO.input(BUTTON_PIN):
            session_end = datetime.now()
            duration = (session_end - session_start).seconds / 60
            log_session_data(session_start.strftime('%Y-%m-%d %H:%M:%S'), duration, eyes_open, not bad_posture, alert_count, water_count)
            print("Session ended.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    df = pd.DataFrame(session_data)
    file_name = "session_data.xlsx"
    if os.path.exists(file_name):
        existing_df = pd.read_excel(file_name)
        df = pd.concat([existing_df, df], ignore_index=True)
    df.to_excel(file_name, index=False)
    print("Session data saved to session_data.xlsx.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    lcd.clear()
