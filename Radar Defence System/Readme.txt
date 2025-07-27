# 🛡️ Radar Defense & Fire Detection System

![Arduino](https://img.shields.io/badge/Arduino-Uno-blue?style=flat-square&logo=arduino)
![Processing](https://img.shields.io/badge/Processing-GUI-lightgrey?style=flat-square&logo=processing)
![Status](https://img.shields.io/badge/Status-Working-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> 🎯 A real-time radar-based detection system with automated laser targeting and visual feedback. Built using Arduino and Processing.

---

## 🔍 Project Description

The **Radar Defense & Fire Detection System** uses an ultrasonic sensor mounted on a servo to scan a 180° field of view. Upon detecting an object within a predefined range, the system locks a secondary servo to the angle of detection and fires a laser at the target.

All scanning and detection data are visualized on a real-time **radar-style GUI** built using the **Processing** IDE.

---

## 🚀 Features

- ✨ **Ultrasonic Object Scanning**  
  Sweep from 0° to 180° with distance tracking at each step.

- 🎯 **Laser Targeting**  
  Automatically aims and activates a laser when an object is detected.

- 📡 **Radar Visualization**  
  Real-time radar interface using Processing to display object positions.

- 🕹️ **Joystick Manual Mode (Optional)**  
  Switch to manual aiming using a joystick for fine targeting.

- 🧩 **Modular Code Structure**  
  Clean, organized `.h/.cpp` files for better readability and maintainability.

---

## 🧰 Technologies Used

| Component         | Purpose                                |
|------------------|----------------------------------------|
| Arduino UNO/Mega | Main controller                        |
| HC-SR04          | Ultrasonic object detection            |
| Servo Motors     | Rotating sensor and aiming laser       |
| Laser Module     | Target illumination or simulation      |
| Processing IDE   | Radar-style visual output              |
| Joystick (opt)   | Manual override for targeting          |

---

## 🎯 System Workflow

---

## 📸 Screenshots *(optional)*

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Radar_animation.gif/440px-Radar_animation.gif" width="300"/>
  <br/>
  <em>Radar-style Visualization in Processing</em>
</p>

---

## 🛠️ Getting Started

### ✅ Requirements
- Arduino IDE
- Processing IDE
- Servo motors ×2
- Ultrasonic sensor (HC-SR04)
- Laser module
- Joystick module (optional)

### 🚦 Upload Arduino Code
```bash
1. Open `main.ino` in Arduino IDE.
2. Ensure all `.cpp` and `.h` files are in the same folder.
3. Upload to your Arduino board.


1. Open `radar_visualizer.pde` in Processing IDE.
2. Update the COM port (e.g., "COM3", "/dev/ttyUSB0").
3. Run the sketch to start visual radar.


📁 AdvancedDefenseSystem/
├── Arduino/
│   ├── main.ino
│   ├── RadarScanner.cpp / .h
│   ├── ManualControl.cpp / .h
│   └── Utilities.cpp / .h
└── Processing/
    └── radar_visualizer.pde


🌱 Future Improvements
🔔 Add buzzer for audio alerts

🔌 Bluetooth/Wi-Fi for remote monitoring

🎥 ESP32-CAM for visual recognition

🤖 AI-based object classification

🔋 Battery-powered deployment mode

