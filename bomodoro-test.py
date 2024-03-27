import tkinter as tk
import time

class FloatingTimer:
    def __init__(self, master):
        self.master = master
        self.master.overrideredirect(True)  # Remove window decorations
        self.master.attributes('-topmost', True)  # Keep window on top
        self.master.geometry("200x100+100+100")  # Set initial position and size
        self.label = tk.Label(master, text="00:00:00", font=("Helvetica", 20))
        self.label.pack(expand=True)
        self.start_time = None
        self.update_time()

    def update_time(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            hours, rem = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            self.label.config(text="{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
        self.master.after(100, self.update_time)

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.start_time = None

if __name__ == "__main__":
    root = tk.Tk()
    timer = FloatingTimer(root)

    def start():
        timer.start_timer()

    def stop():
        timer.stop_timer()

    start_button = tk.Button(root, text="Start", command=start)
    start_button.pack(side=tk.LEFT, padx=10)
    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()
