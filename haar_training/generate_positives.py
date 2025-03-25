"""
This script generates the 'info.dat' file, containing annotations for positive samples.
Each line format:
<relative_path> 1 x y width height

Usage:
    python generate_positives.py
"""

import os
import cv2

def generate_info_dat(positive_folder, annotations_folder, output_file):
    """
    Generates info.dat by combining image paths with annotations (bounding boxes).

    Args:
        positive_folder (str): Path to the folder containing positive images.
        annotations_folder (str): Path to annotation text files (same name as image but .txt).
        output_file (str): Path to output info.dat file.
    """
    with open(output_file, 'w') as out_file:
        for img_file in os.listdir(positive_folder):
            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(positive_folder, img_file).replace('\\', '/')
                annotation_path = os.path.join(annotations_folder, os.path.splitext(img_file)[0] + '.txt')
                if os.path.exists(annotation_path):
                    with open(annotation_path, 'r') as anno_file:
                        bbox = anno_file.readline().strip()  # Expecting format: x y width height
                        out_file.write(f"{img_path} 1 {bbox}\n")
    print(f"[INFO] info.dat generated at {output_file}")

if __name__ == "__main__":
    POSITIVE_FOLDER = 'positives/phone_images'     # Folder with positive images
    ANNOTATIONS_FOLDER = 'positives/annotations'   # Folder with matching annotation .txt files
    OUTPUT_FILE = 'info.dat'                       # Output file for positive samples

    generate_info_dat(POSITIVE_FOLDER, ANNOTATIONS_FOLDER, OUTPUT_FILE)
