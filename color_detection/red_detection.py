import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import numpy as np
from utils.video_utils import capture_image
from utils.logger import log_event

def detect_red():
    # Start video capture from webcam
    cap = cv2.VideoCapture(0)
    log_event("Started Red Color Detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to HSV color space for better color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red color range (tuned for better accuracy)
        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        # Create masks for red
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        red_mask = cv2.bitwise_or(mask1, mask2)

        # Extract red color
        red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Optional: Convert background to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        final = np.where(red_result > 0, red_result, gray)

        cv2.imshow("Red Color Detection", final)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            capture_image(final, "red_detected")

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Red Color Detection")

if __name__ == "__main__":
    detect_red()
