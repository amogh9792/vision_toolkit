import cv2
import os
from datetime import datetime

def capture_image(frame, prefix):
    """
    Captures the current video frame and saves it as an image in the snapshots folder.

    Args:
        frame (numpy.ndarray): The video frame to save.
        prefix (str): A label prefix for the saved image filename.

    Returns:
        None
    """
    # Create snapshots directory if it doesn't exist
    if not os.path.exists("snapshots"):
        os.makedirs("snapshots")
    
    # Generate filename with timestamp
    filename = f"snapshots/{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    
    # Save the image frame
    cv2.imwrite(filename, frame)
    print(f"✅ Snapshot saved: {filename}")
