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

from screenshot import (
    capture_primary_monitor,
    capture_region,
)

from window import get_active_window_rect


def capture(mode: str):

    if mode == "monitor":
        return capture_primary_monitor()

    elif mode == "window":
        return capture_active_window()

    elif mode == "desktop":
        log_info("Entire Desktop capture not implemented yet.")
        log_info("Using Primary Monitor instead.")
        return capture_primary_monitor()

    else:
        log_info("Unknown capture mode.")
        log_info("Using Primary Monitor instead.")
        return capture_primary_monitor()


def capture_active_window():

    left, top, right, bottom = get_active_window_rect()

    return capture_region(
        left,
        top,
        right,
        bottom
    )