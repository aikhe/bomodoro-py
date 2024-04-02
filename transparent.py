from tkinter import *

root = Tk()
root.overrideredirect(True)  # Removes window decorations
root.geometry('500x250')
root.wait_visibility(root)
root.wm_attributes('-transparentcolor', 'red')

frame = Frame(root, bg="red")  # Create a frame to hold your widgets
frame.pack(fill="both", expand=True)

# Add your widgets to the frame here

root.mainloop()

