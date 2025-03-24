import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
from utils.logger import log_event

def eye_detection():
    """
    Detects eyes from the webcam feed within detected face regions.
    """
    face_cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_frontalface_default.xml'))
    eye_cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_eye.xml'))

    log_event(f"Using face cascade: {face_cascade_path}")
    log_event(f"Using eye cascade: {eye_cascade_path}")

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    if face_cascade.empty() or eye_cascade.empty():
        log_event("Error loading cascades.")
        sys.exit("Failed to load Haar cascades.")

    log_event("Started Eye Detection")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

        cv2.imshow('Eye Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Eye Detection")

if __name__ == "__main__":
    eye_detection()