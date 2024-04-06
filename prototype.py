from os import walk

import customtkinter as ctk
from PIL import Image, ImageTk
from rich import print as rprint


class Bomb:
    def __init__(self, parent, img_path, screen_size) -> None:
        self.parent = parent
        self.screen_size = screen_size

        self.explosion_frames = self.import_imgs(img_path)
        self.frm_index = 8
        self.animation_len = len(self.explosion_frames) - 1

        self.label = ctk.CTkLabel(self.parent, text="", image=self.explosion_frames[5])
        self.label.pack(expand=True, fill="both")

        self.animate_explosion()

    def import_imgs(self, img_path) -> list:
        img_paths = []
        for _, __, img_data in walk(img_path):
            sorted_data = sorted(
                img_data, key=lambda item: int(item.split(".")[0][-3:])
            )
            full_path_data = [img_path + "/" + i for i in sorted_data]
            for i in full_path_data:
                img_paths.append(i)

        ctk_imgs = []
        for img in img_paths:
            frame = Image.open(img)
            resized_frm = frame.resize(self.screen_size)
            converted_frm = ImageTk.PhotoImage(resized_frm)

            # ctk_img = ctk.CTkLabel(self.parent, text="", image=converted_frm)
            ctk_imgs.append(converted_frm)

        return ctk_imgs

    def animate_explosion(self):
        if self.frm_index < self.animation_len:
            frame_label = self.label
            self.frm_index += 1

            frame_label.configure(image=self.explosion_frames[self.frm_index])
            frame_label.after(43, self.animate_explosion)

            if self.frm_index == self.animation_len:
                self.parent.destroy()


def main(**kwargs) -> None:
    parent = kwargs.get("master")

    px = kwargs.get("screen_size")
    parent.overrideredirect(True)
    parent.attributes('-topmost', True)
    parent.geometry(f"{px[0]}x{px[1]}")

    Bomb(parent, kwargs.get("frames_path"), px)

    parent.mainloop()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    root.title("Explosion Prototype")

    resolution = (720, 720)
    explosion_path = "./assets/explosion"

    main(master=root, frames_path=explosion_path, screen_size=resolution)
