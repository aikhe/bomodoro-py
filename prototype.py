from tkinter import *
from tkinter import ttk

def main(self) -> None:
  self.title("Bomodoro prototype")
  self.attributes('-topmost', True)
  # self.overrideredirect(True)

  frame = ttk.Frame(self, padding="5")
  img_frame = ttk.Frame(frame, borderwidth=10, relief="ridge", width=200, height=100)
  # img = ttk.Label(img_frame, text="img").grid(column=0, row=0)

  # recreation = StringVar()
  # rct_entry = ttk.Entry(frame, width=10, textvariable=recreation)
  # rct_entry.grid(column=0, row=1)

  # ttk.Label(frame, text="Recreation").grid(column=1, row=1)
  
  # for child in frame.winfo_children():
  #   child.grid_configure(padx=5, pady=5)
  
  frame.grid(column=0, row=0, sticky=(N, S, E, W))
  img_frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

  root.columnconfigure(0, minsize=100, weight=1)
  root.rowconfigure(0, minsize=200, weight=1)
  frame.columnconfigure(0, weight=4)
  frame.rowconfigure(1, weight=1)

  # rct_entry.focus()
  self.mainloop()

  return 0


if __name__ == "__main__":
  root = Tk()
  root.columnconfigure(1, minsize=100, weight=1)
  root.rowconfigure(1, minsize=200, weight=1)

  main(root)
  