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
# get_active_window_title()
#
# ============================================================

import ctypes
from ctypes import wintypes


def _get_foreground_window():

    user32 = ctypes.windll.user32

    hwnd = user32.GetForegroundWindow()

    if hwnd == 0:
        raise RuntimeError("No active window found.")

    return user32, hwnd


def get_active_window_rect():

    user32, hwnd = _get_foreground_window()

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


def get_active_window_title():

    user32, hwnd = _get_foreground_window()

    length = user32.GetWindowTextLengthW(hwnd)

    buffer = ctypes.create_unicode_buffer(length + 1)

    user32.GetWindowTextW(
        hwnd,
        buffer,
        length + 1
    )

    title = buffer.value.strip()

    if title == "":
        return "<untitled>"

    return title