import cv2
import numpy as np

def detect_blue():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Blue color range
        lower_blue = np.array([100, 150, 50])
        upper_blue = np.array([140, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Blue Detection", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_blue()
