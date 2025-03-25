import os
import cv2
img_path = 'haar_training/positives/phones139.png'
print("Exists:", os.path.exists(img_path))  # Should be True
img = cv2.imread(img_path)
if img is None:
    print(f"Failed to load image: {img_path}")
