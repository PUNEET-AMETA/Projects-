Study Assistant — Smart Productivity Monitor

Study Assistant is a Raspberry Pi–powered smart assistant designed to help students develop healthier study habits by minimizing distractions, improving posture, and maintaining hydration in real time.

Project Description

Study Assistant is an AI-powered, real-time monitoring system that observes students during their study sessions. It detects inattention, sleepiness, poor posture, and long sedentary periods, offering timely alerts to keep users productive and healthy. It also reminds users to take hydration and posture breaks.

This system combines computer vision, sensor feedback, and behavioral tracking to create a supportive and focused study environment.

Key Features

Face and Eye Detection: Alerts the user when they are drowsy, inattentive, or not facing the screen.

Posture Monitoring: Identifies slouching or leaning using camera-based posture assessment and prompts correction reminders.

Study Session Timer with Logs: Tracks and records session duration, focus time, and distractions in an Excel (.xlsx) file for review.

Hydration and Break Reminders: Provides periodic water and sedentary break reminders using visual and audio feedback.

Real-Time LCD Display: Displays session time, break timers, and alerts on a 20x4 LCD screen.

Audio Feedback: Provides voice prompts or sound alerts for user interaction and reminders.

Technologies Used

Raspberry Pi: Central processing unit  
Python (OpenCV): Face and eye detection  
PiCamera: Live video feed for posture and eye tracking  
20x4 LCD: Visual output for timer and notifications  
Push Buttons: Manual control for starting and stopping sessions  
Speaker: Audio alerts and reminders  
Excel (openpyxl): Data logging of session activity  

System Workflow

1. User presses a button to start a study session.
2. System activates PiCamera and starts:
   - Face and eye detection
   - Posture detection
   - Session duration tracking
3. Alerts are sent via speaker and LCD if:
   - User looks away or eyes close for too long
   - User slouches or bends
   - Break time or water reminder is due
4. All data is logged into an Excel file for review.
5. User presses the button again to end the session.

Achievements

Successfully implemented live face and eye tracking  
Integrated posture detection using real-time camera data  
Logged detailed session data into Excel with timestamps  
Improved focus and discipline across multiple user trials  

Setup Instructions

Requirements:
- Raspberry Pi 3 or 4 with Raspbian OS  
- Python 3.x  
- PiCamera enabled  
- LCD (20x4) connected via I2C  

Install Dependencies:
pip install opencv-python openpyxl pygame RPi.GPIO

Run the Program:
python3 main.py

Future Enhancements

Graphical dashboard for analytics and insights  
Weekly and monthly productivity tracking with visual graphs  
Mobile application integration for remote monitoring and alerts  
Battery-powered standalone device for portability  
Face recognition for personalized user tracking  
Cloud-based data storage and synchronization  
AI-based adaptive reminders based on user behavior  
Voice assistant integration for interactive control  

“Don’t just study harder. Study smarter.”

