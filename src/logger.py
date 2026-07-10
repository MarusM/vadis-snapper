from datetime import datetime
from pathlib import Path

# ============================================================
# V.A.D.I.S. Logger
# Version 1.0
# ============================================================

LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)


def _write(level: str, message: str) -> None:
    """
    Internal log writer.
    """

    logfile = LOG_FOLDER / f"{datetime.now():%Y-%m-%d}.log"

    timestamp = datetime.now().strftime("%H:%M:%S")

    with logfile.open("a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {level:<7} {message}\n")


def log_info(message: str) -> None:
    _write("INFO", message)


def log_warning(message: str) -> None:
    _write("WARNING", message)


def log_error(message: str) -> None:
    _write("ERROR", message)