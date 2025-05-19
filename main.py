import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize Mediapipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Timing control
prev_action_time = 0
cooldown = 1  # seconds

def is_fist(hand_landmarks):
    # Compare y-coordinates of finger tips and PIP joints to detect closed hand (fist)
    tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky finger tips
    folded = 0

    for tip in tips:
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y:
            folded += 1

    return folded >= 3  # If 3+ fingers are folded, assume a fist

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_fist(hand_landmarks):
                current_time = time.time()
                if current_time - prev_action_time > cooldown:
                    pyautogui.press("space")  # Jump
                    prev_action_time = current_time
                    cv2.putText(img, "JUMP", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Dino Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
