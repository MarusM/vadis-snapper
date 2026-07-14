# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# screenshot.py
#
# Responsibility:
# Creates and stores screenshots.
#
# Public API:
#
# capture_primary_monitor()
# capture_region(left, top, right, bottom)
# capture_entire_desktop()
#
# ============================================================

from datetime import datetime
from pathlib import Path

from PIL import ImageGrab


SCREENSHOT_FOLDER = Path("screenshots")
SCREENSHOT_FOLDER.mkdir(exist_ok=True)


def _create_filename() -> Path:

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")

    return SCREENSHOT_FOLDER / filename


def capture_primary_monitor() -> str:
    """
    Captures the primary monitor.
    """

    image = ImageGrab.grab()

    filepath = _create_filename()

    image.save(filepath)

    return str(filepath)


def capture_region(
    left: int,
    top: int,
    right: int,
    bottom: int
) -> str:
    """
    Captures a rectangular screen region.
    """

    image = ImageGrab.grab(
        bbox=(
            left,
            top,
            right,
            bottom
        )
    )

    filepath = _create_filename()

    image.save(filepath)

    return str(filepath)


def capture_entire_desktop() -> str:
    """
    Captures all connected monitors as one image.
    """

    image = ImageGrab.grab(all_screens=True)

    filepath = _create_filename()

    image.save(filepath)

    return str(filepath)