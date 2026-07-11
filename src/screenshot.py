# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# screenshot.py
#
# Responsibility:
# Creates and stores screenshots.
#
# ============================================================

from datetime import datetime
from pathlib import Path

from PIL import ImageGrab


SCREENSHOT_FOLDER = Path("screenshots")
SCREENSHOT_FOLDER.mkdir(exist_ok=True)


def capture_screen() -> str:
    """
    Creates a screenshot, stores it as PNG and
    returns the filename.
    """

    image = ImageGrab.grab()

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")

    filepath = SCREENSHOT_FOLDER / filename

    image.save(filepath)

    return str(filepath)