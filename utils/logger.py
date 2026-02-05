from datetime import datetime
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log(message):
    """Write logs to logs/redviper.log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file_path = "logs/redviper.log"

    with open(log_file_path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
