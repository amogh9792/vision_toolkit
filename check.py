vec_file = 'haar_training/positives.vec'

with open(vec_file, 'rb') as f:
    f.read(8)  # Skip first 8 bytes
    sample_count = int.from_bytes(f.read(4), byteorder='little')

print(f"[INFO] positives.vec contains {sample_count} samples")
