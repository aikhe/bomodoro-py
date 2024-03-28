from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def main(self) -> None:
  self.title("Bomodoro prototype")
  self.attributes('-topmost', True)
  self.geometry("340x340")
  # self.overrideredirect(True)

  frame = ttk.Frame(self, padding="5")
  # img_frame = ttk.Frame(frame, borderwidth=10, relief="ridge", width=200, height=100)

  photo2 = Image.open("./bomodoro.png")
  resized_image = photo2.resize((340,340))
  converted_image= ImageTk.PhotoImage(resized_image)

  label = ttk.Label(self, image= converted_image)
  label.pack()

  self.mainloop()


if __name__ == "__main__":
  root = Tk()
  root.columnconfigure(1, minsize=100, weight=1)
  root.rowconfigure(1, minsize=200, weight=1)

  main(root)
  

