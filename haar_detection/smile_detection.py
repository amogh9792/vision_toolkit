import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
from utils.logger import log_event

def smile_detection():
    """
    Detects smiles within detected face regions from the webcam feed.
    """
    face_cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_frontalface_default.xml'))
    smile_cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_smile.xml'))

    log_event(f"Using face cascade: {face_cascade_path}")
    log_event(f"Using smile cascade: {smile_cascade_path}")

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

    if face_cascade.empty() or smile_cascade.empty():
        log_event("Error loading cascades.")
        sys.exit("Failed to load Haar cascades.")

    log_event("Started Smile Detection")
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
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

            if len(smiles) > 0:
                cv2.putText(frame, "Smiling", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

        cv2.imshow('Smile Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Smile Detection")

if __name__ == "__main__":
    smile_detection()