import tkinter as tk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

root = tk.Tk()
root.attributes("-transparentcolor", "white")  # Make white background transparent

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

rounded_button = create_rounded_rectangle(canvas, 10, 10, 190, 90, 10, fill="blue")
canvas.create_text(100, 50, text="Click me!", fill="white")

root.mainloop()
