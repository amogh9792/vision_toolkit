import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
from utils.logger import log_event

def face_detection():
    # Dynamically get the absolute path to haarcascade file inside haar_detection/haar_cascades
    cascade_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'haar_cascades', 'haarcascade_frontalface_default.xml'))

    # Check if the cascade file exists
    if not os.path.exists(cascade_path):
        print("[ERROR]: Haar Cascade XML file not found.")
        return

    face_cascade = cv2.CascadeClassifier(cascade_path)
    if face_cascade.empty():
        print("[ERROR]: Failed to load Haar Cascade.")
        return

    cap = cv2.VideoCapture(0)
    log_event("Started Face Detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_detection()
