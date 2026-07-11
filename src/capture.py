# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# capture.py
#
# Responsibility:
# Communicates with the operating system.
# Retrieves information about the active window.
#
# ============================================================

import ctypes


def get_active_window_title() -> str:

    user32 = ctypes.windll.user32

    hwnd = user32.GetForegroundWindow()

    if hwnd == 0:
        return "No active window"

    length = user32.GetWindowTextLengthW(hwnd)

    buffer = ctypes.create_unicode_buffer(length + 1)

    user32.GetWindowTextW(hwnd, buffer, length + 1)

    title = buffer.value.strip()

    if title == "":
        return "Untitled window"

    return title