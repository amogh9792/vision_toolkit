"""
Generates bg.txt file containing paths to negative images for Haar Cascade training.

Usage:
    python create_bg_txt.py
"""

import os

def create_bg_file(neg_folder, output_file):
    """
    Creates a bg.txt file listing all negative images.

    Args:
        neg_folder (str): Path to the folder containing negative images.
        output_file (str): Output bg.txt file path.
    """
    with open(output_file, "w") as f:
        for img_file in os.listdir(neg_folder):
            if img_file.endswith(('.jpg', '.png', '.jpeg')):
                # Convert Windows backslashes to forward slashes for compatibility
                img_path = os.path.join(neg_folder, img_file).replace("\\", "/")
                f.write(f"{img_path}\n")
    print(f"[INFO] bg.txt created at {output_file}")

if __name__ == "__main__":
    NEG_FOLDER = "negatives"        # Replace with your negatives folder if different
    OUTPUT_FILE = "bg.txt"
    create_bg_file(NEG_FOLDER, OUTPUT_FILE)
