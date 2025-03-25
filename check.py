import os

with open('haar_training/info.dat', 'r') as f:
    for idx, line in enumerate(f, 1):
        img_path = line.strip().split(' ')[0]
        if not os.path.exists(img_path):
            print(f"[MISSING] Line {idx}: {img_path}")
