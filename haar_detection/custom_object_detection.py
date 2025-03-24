import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
from utils.logger import log_event

def custom_object_detection():
    """
    Perform real-time detection of a custom object using a trained Haar cascade XML.
    Replace 'custom_cascade.xml' with your trained Haar XML file.
    """
    # Path to the custom Haar cascade XML
    custom_cascade_path = os.path.join(os.path.dirname(__file__), 'haar_cascades', 'custom_cascade.xml')
    log_event(f"Using custom cascade path: {custom_cascade_path}")

    # Check if the cascade file exists
    if not os.path.exists(custom_cascade_path):
        log_event("Custom Haar cascade file not found!")
        return

    # Load the trained Haar cascade
    custom_cascade = cv2.CascadeClassifier(custom_cascade_path)

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    log_event("Started Custom Object Detection")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect custom objects in the frame
        objects = custom_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw rectangles around detected objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Object Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 0, 255), 2)

        # Display the result
        cv2.imshow('Custom Object Detection', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    log_event("Stopped Custom Object Detection")

if __name__ == '__main__':
    custom_object_detection()
