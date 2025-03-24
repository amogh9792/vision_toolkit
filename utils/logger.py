from datetime import datetime

def log_event(message):
    """
    Logs an event message with a timestamp to the vision_toolkit.log file.

    Args:
        message (str): The message to log.

    Returns:
        None
    """
    log_filename = 'vision_toolkit.log'
    
    # Append the log entry to the log file with a timestamp
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")
    
    # Optional: Also print to console for real-time feedback
    print(f"[LOG]: {message}")
