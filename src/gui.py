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

    image = capture_screen()

    if image is not None:
        log_info("Screenshot successfully created.")
    else:
        log_info("Screenshot creation failed.")

    status_label.after(
        500,
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

    status = tk.Label(
        root,
        text="Ready",
        fg="gray"
    )

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

    status.pack(
        side="bottom",
        pady=15
    )

    root.mainloop()