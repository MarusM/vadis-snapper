# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# logger.py
#
# Responsibility:
# Writes application log messages.
#
# ============================================================

from datetime import datetime
from pathlib import Path

from session import SESSION_ID


LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)


LOGFILE = LOG_FOLDER / f"{SESSION_ID}.log"


def _write(level: str, message: str):

    timestamp = datetime.now().strftime("%H:%M:%S")

    with LOGFILE.open("a", encoding="utf-8") as file:

        file.write(
            f"[{timestamp}] {level:<7} {message}\n"
        )


def log_info(message: str):

    _write("INFO", message)


def log_warning(message: str):

    _write("WARNING", message)


def log_error(message: str):

    _write("ERROR", message)