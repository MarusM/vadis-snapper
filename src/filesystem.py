# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# filesystem.py
#
# Responsibility:
# File system related helper functions.
#
# ============================================================

import os
from pathlib import Path

from logger import log_info


SCREENSHOT_FOLDER = Path("screenshots")


def open_screenshot_folder():

    SCREENSHOT_FOLDER.mkdir(exist_ok=True)

    log_info("Opening screenshot folder.")

    os.startfile(SCREENSHOT_FOLDER)