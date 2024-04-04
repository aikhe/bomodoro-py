import customtkinter as ctk

class Bomb:
    def __init__(self, parent) -> None:
        self.parent = parent

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("430x430")

    Bomb(root)

    root.mainloop()
