# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# gui.py
#
# Responsibility:
# Creates and manages the graphical user interface.
#
# ============================================================

import tkinter as tk

from logger import log_info
from screenshot import capture_screen


def on_snap(status_label):

    status_label.config(text="Capturing...")

    try:

        filename = capture_screen()

        log_info(f"Screenshot saved: {filename}")

        status_label.config(text="Screenshot saved")

    except Exception as error:

        log_info(f"Screenshot failed: {error}")

        status_label.config(text="Capture failed")

    status_label.after(
        1200,
        lambda: status_label.config(text="Ready")
    )


def run_gui():

    root = tk.Tk()

    root.title("V.A.D.I.S. Snapper")
    root.geometry("420x220")
    root.minsize(420, 220)

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = tk.Label(
        root,
        text="V.A.D.I.S. Snapper",
        font=("Segoe UI", 16, "bold")
    )

    title.pack(pady=(20, 15))

    # --------------------------------------------------------
    # Snap Button
    # --------------------------------------------------------

    snap_button = tk.Button(
        root,
        text="SNAP",
        width=20,
        height=2,
        command=lambda: on_snap(status)
    )

    snap_button.pack()

    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    status = tk.Label(
        root,
        text="Ready",
        fg="gray"
    )

    status.pack(
        side="bottom",
        pady=15
    )

    root.mainloop()