import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import numpy as np
from utils.video_utils import capture_image
from utils.logger import log_event

def detect_blue():
    # Start webcam
    cap = cv2.VideoCapture(0)
    log_event("Started Blue Color Detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Blue color range
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])

        # Create mask for blue
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        blue_result = cv2.bitwise_and(frame, frame, mask=mask)

        # Optional: Convert background to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        final = np.where(blue_result > 0, blue_result, gray)

        cv2.imshow("Blue Color Detection", final)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            capture_image(final, "blue_detected")

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Blue Color Detection")

if __name__ == "__main__":
    detect_blue()
