# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# window.py
#
# Responsibility:
# Operating system interface for window information.
#
# Public API:
#
# get_active_window_rect()
#
# ============================================================

import ctypes
from ctypes import wintypes


def get_active_window_rect():
    """
    Returns the rectangle of the currently
    active foreground window.

    Returns:
        (left, top, right, bottom)

    Raises:
        RuntimeError
            if no active window is available.
    """

    user32 = ctypes.windll.user32

    hwnd = user32.GetForegroundWindow()

    if hwnd == 0:
        raise RuntimeError("No active window found.")

    rect = wintypes.RECT()

    success = user32.GetWindowRect(
        hwnd,
        ctypes.byref(rect)
    )

    if not success:
        raise RuntimeError("Unable to retrieve window rectangle.")

    return (
        rect.left,
        rect.top,
        rect.right,
        rect.bottom
    )