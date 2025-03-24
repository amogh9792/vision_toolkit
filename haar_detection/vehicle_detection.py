import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
from utils.logger import log_event

def vehicle_detection():
    """
    Detects vehicles using a Haar cascade classifier.
    """
    vehicle_cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_car.xml'))

    log_event(f"Using vehicle cascade: {vehicle_cascade_path}")

    vehicle_cascade = cv2.CascadeClassifier(vehicle_cascade_path)

    if vehicle_cascade.empty():
        log_event("Error loading vehicle cascade.")
        sys.exit("Failed to load Haar cascade for vehicles.")

    log_event("Started Vehicle Detection")

    # You can replace 0 with a video file path for vehicle footage
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('Vehicle Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Vehicle Detection")

if __name__ == "__main__":
    vehicle_detection()