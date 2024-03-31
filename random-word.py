import tkinter as tk
import random
import time

class RandomWordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Word App")
        
        self.label = tk.Label(self.master, text="")
        self.label.pack()
        
        self.words = ["apple", "banana", "orange", "grape", "pineapple"]
        
        self.change_word()

    def change_word(self):
        self.label.config(text=random.choice(self.words))
        self.master.after(2000, self.change_word)

def main():
    root = tk.Tk()
    app = RandomWordApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
