from rich import print as rprint

import customtkinter as ctk
from PIL import Image, ImageTk
from os import walk

class Bomb:
    def __init__(self, parent, img_path) -> None:
        self.parent = parent

        explosion_frames = self.import_imgs(img_path)

        label = explosion_frames[34]
        label.pack(expand=True, fill="both")

    def import_imgs(self, img_path) -> list:
        img_paths = []
        for _, __, img_data in walk(img_path):
            sorted_data = sorted(
				img_data, 
				key = lambda item: int(item.split('.')[0][-3:])
            )
            full_path_data = [img_path + '/' + i for i in sorted_data]
            for i in full_path_data:
                img_paths.append(i)

        ctk_imgs = []
        for img in img_paths:
            frame = Image.open(img)
            resized_frm = frame.resize((340, 340))
            converted_frm = ImageTk.PhotoImage(resized_frm)

            ctk_img = ctk.CTkLabel(
                self.parent,
                text = "",
                image = converted_frm
            )
            ctk_imgs.append(ctk_img)

        return(ctk_imgs)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Explosion Prototype")
    root.geometry("430x430")

    explosion = './assets/explosion'
    Bomb(root, explosion)

    root.mainloop()
