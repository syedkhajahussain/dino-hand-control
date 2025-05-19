# Dino Hand Control

Control the Google Chrome Dino game using your hand gestures with Python, OpenCV, and MediaPipe!

## 📸 What It Does

- Detects your hand via webcam.
- Uses a closed fist gesture to trigger a jump in the Dino game.
- No keyboard needed — just your hand!

## 🧰 Built With

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## 🚀 Getting Started

### 📦 Prerequisites

Install Python dependencies:

```bash
pip install opencv-python mediapipe pyautogui

#Run the Script
python main.py
Make sure your webcam is working and accessible.

🕹️ How to Play
Open Google Chrome and go to: chrome://dino

Start the game by pressing the spacebar once.

Run the script above.

Show a fist to the webcam to jump.

Press q to quit the program.

🤖 How It Works
The script uses MediaPipe to detect hand landmarks.

If 3 or more fingers are folded (closed fist), it simulates a space key press using pyautogui.
