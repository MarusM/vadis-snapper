import tkinter as tk


root = tk.Tk()

root.title("V.A.D.I.S. Snapper")
root.geometry("420x220")
root.minsize(420, 220)

# ---------- Title ----------

title = tk.Label(
    root,
    text="V.A.D.I.S. Snapper",
    font=("Segoe UI", 16, "bold")
)

title.pack(pady=(20, 15))

# ---------- Snap Button ----------

snap_button = tk.Button(
    root,
    text="SNAP",
    width=20,
    height=2
)

snap_button.pack()

# ---------- Status ----------

status = tk.Label(
    root,
    text="Ready",
    fg="gray"
)

status.pack(side="bottom", pady=15)

root.mainloop()