# import tkinter as tk
# from tkinter import ttk

import tkinter as tk
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text='{:02d}:{:02d}'.format(mins, secs))
        root.update()
        time.sleep(1)
        seconds -= 1
    timer_label.config(text="Boom!")

root = tk.Tk()
root.overrideredirect(True)  # Remove window decorations
root.wait_visibility(root)
root.wm_attributes('-alpha',0.3)

timer_label = tk.Label(root, font=('Arial', 24))
timer_label.pack(padx=20, pady=10)

# Set timer to 99 minutes
countdown(99)

root.mainloop()

