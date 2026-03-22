
import logging
import os


LOGS_FOLDER = "logs"
LOG_FILE = os.path.join(LOGS_FOLDER, "jarvis.log")

# Create logs/ folder automatically if not exists
if not os.path.exists(LOGS_FOLDER):
    os.makedirs(LOGS_FOLDER)


def setup_logger():
   

    logger = logging.getLogger("Jarvis")
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers if called multiple times
    if logger.handlers:
        return logger

    # ── Format for log entries ──────────────────
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ── Handler 1: Save to file ─────────────────
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # ── Handler 2: Print to terminal ────────────
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Attach both handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger



logger = setup_logger()