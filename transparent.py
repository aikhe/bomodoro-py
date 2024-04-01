from tkinter import Tk, Frame, Label

root = Tk()
root.overrideredirect(True)  # Removes window decorations
root.wait_visibility(root)
root.wm_attributes('-alpha', 0.3)

frame = Frame(root, bg="white")  # Create a frame to hold your widgets
frame.pack(fill="both", expand=True)

# Add your widgets to the frame here
label = Label(frame, text="Unaffected Frame")
label.pack()

root.mainloop()
