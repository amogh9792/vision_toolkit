import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to run a script
def run_script(script_path):
    try:
        subprocess.Popen(["python", script_path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start {script_path}\n{e}")

# Create main GUI window
app = tk.Tk()
app.title("Vision Toolkit")
app.geometry("400x500")

tk.Label(app, text="Computer Vision Toolkit", font=("Helvetica", 18)).pack(pady=20)

# Buttons for Color Detection
tk.Button(app, text="Red Color Detection", command=lambda: run_script("color_detection/red_detection.py")).pack(pady=5)
tk.Button(app, text="Blue Color Detection", command=lambda: run_script("color_detection/blue_detection.py")).pack(pady=5)

# Buttons for Haar Detection
tk.Button(app, text="Face Detection", command=lambda: run_script("haar_detection/face_detection.py")).pack(pady=5)
tk.Button(app, text="Eye Detection", command=lambda: run_script("haar_detection/eye_detection.py")).pack(pady=5)
tk.Button(app, text="Smile Detection", command=lambda: run_script("haar_detection/smile_detection.py")).pack(pady=5)
tk.Button(app, text="Vehicle Detection", command=lambda: run_script("haar_detection/vehicle_detection.py")).pack(pady=5)
tk.Button(app, text="Custom Object Detection", command=lambda: run_script("haar_detection/custom_object_detection.py")).pack(pady=5)

app.mainloop()
