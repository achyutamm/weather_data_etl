import logging
import os
from datetime import datetime

def setup_logger(script_name):
    # Create log directory in /tmp with current date
    log_dir = os.path.join("/tmp", datetime.now().strftime("%Y-%m-%d"))
    os.makedirs(log_dir, exist_ok=True)

    # Create log file with current time
    log_file = os.path.join(log_dir, f"{script_name}_{datetime.now().strftime('%H-%M-%S')}.log")

    # Set up logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

    logging.getLogger().addHandler(console_handler)

    return logging.getLogger()
