"""
Real-time Mobile Phone detection using the custom-trained Haar Cascade.

Make sure the path to 'mobile_cascade.xml' is correct.

Usage:
    python haar_detection/mobile_detection.py
"""

import cv2
import sys
import os

# Ensure the parent directory is accessible for utility imports if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Optional logger import if your logger exists
from utils.logger import log_event

def detect_mobile():
    """
    Function to detect mobile phones using a webcam and a custom Haar cascade classifier.
    """
    # Construct the absolute path to your trained cascade XML
    cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'mobile_cascade.xml'))

    # Logging cascade path for debugging
    log_event(f"Using cascade path: {cascade_path}") if 'log_event' in globals() else print(f"[LOG]: Using cascade path: {cascade_path}")

    # Check if the cascade file exists
    if not os.path.exists(cascade_path):
        print(f"[ERROR]: Cascade file not found at {cascade_path}")
        return

    # Load the trained Haar cascade for mobile phone detection
    phone_cascade = cv2.CascadeClassifier(cascade_path)

    # Check if the cascade was loaded properly
    if phone_cascade.empty():
        print("[ERROR]: Failed to load the cascade classifier")
        return

    # Start webcam capture
    cap = cv2.VideoCapture(0)
    log_event("Started Mobile Phone Detection") if 'log_event' in globals() else print("[LOG]: Started Mobile Phone Detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR]: Failed to capture frame from webcam")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect mobile phones in the frame
        mobiles = phone_cascade.detectMultiScale(
            gray,
            scaleFactor=1.4,
            minNeighbors=10,     # Tuned minNeighbors for better accuracy
            minSize=(60, 60)    # Adjust this based on your training dataset
        )

        # Draw rectangles around detected mobiles
        for (x, y, w, h) in mobiles:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Mobile Phone', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Mobile Phone Detection', frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Mobile Phone Detection") if 'log_event' in globals() else print("[LOG]: Stopped Mobile Phone Detection")

if __name__ == "__main__":
    detect_mobile()
