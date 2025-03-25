"""
Automates the training process for the Haar Cascade classifier using OpenCV's opencv_traincascade tool.
After training, renames the generated classifier.xml to mobile_cascade.xml.

Usage:
    python train_cascade.py
"""

import os
import subprocess
import shutil

def train_cascade(positive_vec, bg_file, output_dir, num_pos, num_neg, num_stages, width, height, final_cascade_name):
    """
    Runs opencv_traincascade with provided parameters and renames the final output.

    Args:
        positive_vec (str): Path to .vec file with positive samples.
        bg_file (str): Path to bg.txt file containing negative image paths.
        output_dir (str): Output directory for cascade files.
        num_pos (int): Number of positive samples used.
        num_neg (int): Number of negative samples used.
        num_stages (int): Number of training stages.
        width (int): Width of the sample images.
        height (int): Height of the sample images.
        final_cascade_name (str): Desired name of the final trained cascade XML file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cmd = [
        "opencv_traincascade",
        "-data", output_dir,
        "-vec", positive_vec,
        "-bg", bg_file,
        "-numPos", str(num_pos),
        "-numNeg", str(num_neg),
        "-numStages", str(num_stages),
        "-w", str(width),
        "-h", str(height),
        "-featureType", "HAAR",
        "-mode", "ALL",
        "-precalcValBufSize", "1024",
        "-precalcIdxBufSize", "1024"
    ]

    print(f"[INFO] Running training command:\n{' '.join(cmd)}\n")
    subprocess.run(cmd, shell=True, check=True)

    # After training, rename classifier.xml to desired cascade name
    classifier_path = os.path.join(output_dir, "classifier.xml")
    final_cascade_path = os.path.join(output_dir, final_cascade_name)
    
    if os.path.exists(classifier_path):
        shutil.move(classifier_path, final_cascade_path)
        print(f"[INFO] Training completed. Cascade saved as: {final_cascade_path}")
    else:
        print("[ERROR] Training failed or classifier.xml not found.")

if __name__ == "__main__":
    POS_VEC = os.path.join('haar_training', 'positives.vec')
    BG_FILE = os.path.join('haar_training', 'bg.txt')
    OUTPUT_DIR = os.path.join('haar_training', 'output')
    NUM_POS = 2500    # Should be <= .vec sample count
    NUM_NEG = 2000
    NUM_STAGES = 10   # 10-20 is good, more = better but slower
    WIDTH, HEIGHT = 24, 24  # Match sample size
    FINAL_CASCADE_NAME = "mobile_cascade.xml"  # Final output file name

    train_cascade(POS_VEC, BG_FILE, OUTPUT_DIR, NUM_POS, NUM_NEG, NUM_STAGES, WIDTH, HEIGHT, FINAL_CASCADE_NAME)
