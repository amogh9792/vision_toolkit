"""
Automates the generation of the .vec file required for Haar Cascade training
using OpenCV's opencv_createsamples utility.

Usage:
    python create_samples.py
"""

import os
import subprocess

def create_samples(info_dat, output_vec, num_samples, width, height):
    """
    Runs opencv_createsamples to generate the .vec file.

    Args:
        info_dat (str): Path to info.dat containing positive samples and annotations.
        output_vec (str): Path to the output .vec file.
        num_samples (int): Number of samples to generate.
        width (int): Width of the sample images.
        height (int): Height of the sample images.
    """
    opencv_createsamples_path = r"C:\opencv\build\x64\vc15\bin\opencv_createsamples.exe"
    cmd = [
        opencv_createsamples_path,
        "-info", info_dat,
        "-num", str(num_samples),
        "-w", str(width),
        "-h", str(height),
        "-vec", output_vec
    ]


    print(f"[INFO] Running: {' '.join(cmd)}")
    subprocess.run(cmd, shell=True, check=True)
    print(f"[INFO] {output_vec} file created successfully!")

if __name__ == "__main__":
    INFO_DAT = "info.dat"          # Generated from generate_positives.py
    OUTPUT_VEC = "positives.vec"   # Output vector file
    NUM_SAMPLES = 3000             # Number of positive samples (match or < actual images)
    WIDTH, HEIGHT = 24, 24         # Recommended size (fixed for training)

    create_samples(INFO_DAT, OUTPUT_VEC, NUM_SAMPLES, WIDTH, HEIGHT)
