import customtkinter as ctk  # Import customtkinter
from PIL import Image, ImageTk  # Import from PIL
import tkinter as tk  # Import tkinter for Tk constants

ctk.set_appearance_mode("dark")  # Set theme of customtkinter

# Create the main window
app = ctk.CTk()
app.title('Resize Image in customtkinter')

# Load the image
original_image = Image.open('./assets/better-bomb.png')

# Resize the image to desired dimensions (e.g., 200x200)
resized_image = original_image.resize((200, 200), Image.Resampling.LANCZOS)

# Convert the image to a format tkinter recognizes
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = ctk.CTkLabel(app, image=tk_image)
image_label.pack(pady=20)

app.mainloop()

