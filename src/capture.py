# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# capture.py
#
# Responsibility:
# Capture backend.
#
# Public API:
#
# capture(mode)
#
# ============================================================

from logger import log_info
from screenshot import capture_screen


def capture(mode: str):

    if mode == "monitor":
        return capture_primary_monitor()

    elif mode == "window":
        log_info("Active Window capture not implemented yet.")
        log_info("Using Primary Monitor instead.")
        return capture_primary_monitor()

    elif mode == "desktop":
        log_info("Entire Desktop capture not implemented yet.")
        log_info("Using Primary Monitor instead.")
        return capture_primary_monitor()

    else:
        log_info("Unknown capture mode.")
        log_info("Using Primary Monitor instead.")
        return capture_primary_monitor()


def capture_primary_monitor():

    return capture_screen()