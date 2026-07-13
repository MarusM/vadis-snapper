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

from logger import log_info, log_error
from screenshot import capture_screen
from filesystem import open_screenshot_folder
from session import SESSION_ID
from version import APPLICATION_NAME, BUILD


def on_snap(status_label):

    status_label.config(text="Capturing...")

    try:

        filename = capture_screen()

        log_info(f"Screenshot saved: {filename}")

        status_label.config(text="Screenshot saved")

    except Exception as error:

        log_error(f"Screenshot failed: {error}")

        status_label.config(text="Capture failed")

    status_label.after(
        1200,
        lambda: status_label.config(text="Ready")
    )


def on_open_folder():

    open_screenshot_folder()


def run_gui():

    root = tk.Tk()

    root.title(APPLICATION_NAME)
    root.geometry("430x340")
    root.minsize(430, 340)

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    title = tk.Label(
        root,
        text=APPLICATION_NAME,
        font=("Segoe UI", 16, "bold")
    )

    title.pack(pady=(20, 15))

    # --------------------------------------------------------
    # SNAP
    # --------------------------------------------------------

    snap_button = tk.Button(
        root,
        text="SNAP",
        width=22,
        height=2,
        command=lambda: on_snap(status_value)
    )

    snap_button.pack(pady=(0, 10))

    # --------------------------------------------------------
    # Folder
    # --------------------------------------------------------

    folder_button = tk.Button(
        root,
        text="Open Screenshot Folder",
        width=22,
        command=on_open_folder
    )

    folder_button.pack()

    # --------------------------------------------------------
    # Footer
    # --------------------------------------------------------

    footer = tk.Frame(
        root,
        bd=1,
        relief="sunken"
    )

    footer.pack(
        side="bottom",
        fill="x"
    )

    status_value = tk.Label(
        footer,
        text="Status : Ready",
        anchor="w"
    )

    status_value.pack(
        anchor="w",
        padx=8,
        pady=(6, 0)
    )

    session_value = tk.Label(
        footer,
        text=f"Session: {SESSION_ID}",
        anchor="w",
        font=("Consolas", 9)
    )

    session_value.pack(
        anchor="w",
        padx=8
    )

    build_value = tk.Label(
        footer,
        text=f"Build  : {BUILD}",
        anchor="w",
        font=("Consolas", 9)
    )

    build_value.pack(
        anchor="w",
        padx=8,
        pady=(0, 6)
    )

    root.mainloop()