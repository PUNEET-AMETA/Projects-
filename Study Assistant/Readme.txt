# 🎓 Study Assistant — Smart Productivity Monitor

<img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python" />
<img src="https://img.shields.io/badge/Raspberry%20Pi-Project-red?style=flat-square&logo=raspberry-pi" />
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square" />

> 💡 A Raspberry Pi–powered smart assistant to help students develop **healthier study habits** by minimizing distractions, improving posture, and maintaining hydration—all in real-time!

---

## 🧠 Project Description

**Study Assistant** is an AI-powered, real-time monitoring system that observes students during their study sessions. It detects **inattention**, **sleepiness**, **poor posture**, and **long sedentary periods**, offering timely alerts to keep users productive and healthy. It also reminds users to take hydration and posture breaks.

This system combines **computer vision**, **sensor feedback**, and **behavioral tracking** to create a supportive and focused study environment.

---

## 🚀 Key Features

- 👁️ **Face and Eye Detection**  
  Alerts the user when they are drowsy, inattentive, or not facing the screen.

- 🪑 **Posture Monitoring**  
  Identifies slouching or leaning using camera-based posture assessment, prompting correction reminders.

- ⏱️ **Study Session Timer with Logs**  
  Tracks and records session duration, focus time, and distractions in an **Excel (.xlsx)** file for review.

- 🚰 **Hydration & Break Reminders**  
  Periodic water and sedentary break reminders using visual and audio feedback.

- 📺 **Real-Time LCD Display**  
  Displays session time, break timers, and alerts on a 20x4 LCD screen.

- 🔊 **Audio Feedback**  
  Friendly voice prompts via speakers for user interaction and reminders.

---

## 🧰 Technologies Used

| Technology        | Purpose                                |
|-------------------|----------------------------------------|
| **Raspberry Pi**  | Central processing unit                |
| **Python (OpenCV)** | Face and eye detection                |
| **PiCamera**      | Live video feed for posture and eye tracking |
| **20x4 LCD**      | Visual output for timer and notifications |
| **Push Buttons**  | Manual control for starting/stopping sessions |
| **Speaker**       | Audio alerts and reminders             |
| **Excel (openpyxl)** | Data logging of session activity     |

---

## ⚙️ System Workflow

```
1. User presses a button to start a study session.
2. System activates PiCamera and starts:
   - Face & eye detection (inattention alerts)
   - Posture detection
   - Session duration tracking
3. Alerts sent via speaker + LCD if:
   - User looks away or eyes close for too long
   - User slouches or bends
   - Break time or water reminder is due
4. All data is logged into an Excel file for review.
5. User presses button again to end session.
```

---

## 🏆 Achievements

- ✅ Successfully implemented **live face and eye tracking**.
- ✅ Integrated **posture detection** using real-time camera data.
- ✅ Logged detailed session data into **Excel** with timestamps.
- ✅ Improved focus and discipline across multiple user trials.

---

## 📦 Folder Structure

```
📁 StudyAssistant/
├── main.py
├── eye_tracker.py
├── posture_monitor.py
├── lcd_controller.py
├── logger.py
├── assets/
│   ├── sounds/
│   └── icons/
└── session_data.xlsx
```


## 🛠️ Setup Instructions

### ✅ Requirements

- Raspberry Pi 3/4 with Raspbian OS
- Python 3.x
- PiCamera enabled
- LCD (20x4) connected via I2C
- `openpyxl`, `opencv-python`, `RPi.GPIO`, `pygame`, etc.

### 📦 Install Dependencies

```bash
pip install opencv-python openpyxl pygame RPi.GPIO
```

### ▶️ Run the Program

```bash
python3 main.py
```

---

## 📅 Future Enhancements

- 💻 GUI dashboard for analytics  
- 📈 Weekly focus trend graphs  
- 📱 Mobile app sync with real-time alerts  
- 🔋 Battery-powered standalone operation  
- 🔒 Face recognition for personalized tracking  

---



🧠 *“Don’t just study harder. Study smarter.”*
