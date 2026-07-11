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


SCREENSHOT_FOLDER = Path("screenshots")


def open_screenshot_folder():

    SCREENSHOT_FOLDER.mkdir(exist_ok=True)

    os.startfile(SCREENSHOT_FOLDER)