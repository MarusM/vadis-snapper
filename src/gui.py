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
from capture import capture
from filesystem import open_screenshot_folder
from session import SESSION_ID
from version import APPLICATION_NAME, BUILD
from language import tr


def on_snap(status_label, capture_mode):

    mode = capture_mode.get()

    mode_names = {
        "window": tr("mode.window"),
        "monitor": tr("mode.monitor"),
        "desktop": tr("mode.desktop")
    }

    log_info(f"Capture mode: {mode_names[mode]}")

    status_label.config(text=tr("status.capturing"))

    try:

        filename = capture(mode)

        log_info(f"Screenshot saved: {filename}")

        status_label.config(text=tr("status.saved"))

    except Exception as error:

        log_error(f"Screenshot failed: {error}")

        status_label.config(text=tr("status.failed"))

    status_label.after(
        1200,
        lambda: status_label.config(text=tr("status.ready"))
    )


def on_open_folder():

    open_screenshot_folder()


def run_gui():

    root = tk.Tk()

    root.title(APPLICATION_NAME)
    root.geometry("430x430")
    root.minsize(430, 430)

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
    # Capture Mode
    # --------------------------------------------------------

    capture_mode = tk.StringVar(value="monitor")

    # --------------------------------------------------------
    # SNAP
    # --------------------------------------------------------

    snap_button = tk.Button(
        root,
        text=tr("button.snap"),
        width=22,
        height=2,
        command=lambda: on_snap(status_value, capture_mode)
    )

    snap_button.pack(pady=(0, 15))

    # --------------------------------------------------------
    # Capture Mode
    # --------------------------------------------------------

    mode_frame = tk.LabelFrame(
        root,
        text=tr("group.capture"),
        padx=12,
        pady=8
    )

    mode_frame.pack(
        padx=20,
        fill="x"
    )

    tk.Radiobutton(
        mode_frame,
        text=tr("mode.window"),
        variable=capture_mode,
        value="window"
    ).pack(anchor="w")

    tk.Radiobutton(
        mode_frame,
        text=tr("mode.monitor"),
        variable=capture_mode,
        value="monitor"
    ).pack(anchor="w")

    tk.Radiobutton(
        mode_frame,
        text=tr("mode.desktop"),
        variable=capture_mode,
        value="desktop"
    ).pack(anchor="w")

    # --------------------------------------------------------
    # Folder Button
    # --------------------------------------------------------

    folder_button = tk.Button(
        root,
        text=tr("button.folder"),
        width=22,
        command=on_open_folder
    )

    folder_button.pack(pady=15)

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
        text=tr("status.ready"),
        anchor="w"
    )

    status_value.pack(
        anchor="w",
        padx=8,
        pady=(6, 0)
    )

    session_value = tk.Label(
        footer,
        text=f"Session : {SESSION_ID}",
        anchor="w",
        font=("Consolas", 9)
    )

    session_value.pack(
        anchor="w",
        padx=8
    )

    build_value = tk.Label(
        footer,
        text=f"Build   : {BUILD}",
        anchor="w",
        font=("Consolas", 9)
    )

    build_value.pack(
        anchor="w",
        padx=8,
        pady=(0, 6)
    )

    root.mainloop()