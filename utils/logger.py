import logging
import os
import sys
from datetime import datetime

def setup_logger(logger_name, log_level=logging.INFO, console_level=logging.ERROR, stage_name=""):
    """
    Set up and return a logger with both file and console handlers.

    Args:
        logger_name (str): Name of the logger (used for log file naming).
        log_level (int): Logging level for the file handler (default: logging.INFO).
        console_level (int): Logging level for the console handler (default: logging.ERROR).
        stage_name (str): Custom stage name to include in log messages.

    Returns:
        logging.Logger: Configured logger instance.

    Notes:
        - Log files are saved in the 'logs' folder at the project root.
        - If a logger with the same name already exists, it will be reused.
        - Formatter includes stage name, timestamp, log level, logger name, function name, and message.
    """
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(logs_dir, f"{logger_name}_{timestamp}.log")

    logger = logging.getLogger(logger_name)

    # Avoid adding handlers multiple times if logger already exists
    if not logger.hasHandlers():
        logger.setLevel(log_level)

        formatter = logging.Formatter(
            f"[{stage_name} %(asctime)s] %(levelname)s %(name)s.%(funcName)s: %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # File handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler (no emoji, no stream reassignment)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger