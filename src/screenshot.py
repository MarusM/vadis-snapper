# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# screenshot.py
#
# Responsibility:
# Creates screenshots.
#
# ============================================================

from PIL import ImageGrab


def capture_screen():

    image = ImageGrab.grab()

    return image