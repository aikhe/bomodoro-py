from os import walk

import customtkinter as ctk
from PIL import Image, ImageTk
from pygame import mixer
import threading
import time
from rich import print as rprint


class Bomb:
    def __init__(self, parent, img_path, screen_size) -> None:
        self.parent = parent
        self.screen_size = screen_size

        self.explosion_frames = self.import_imgs(img_path)
        self.frm_index = 2
        self.animation_len = len(self.explosion_frames) - 1

    def initialize_gui(self, win, res) -> None:
        # raise NotImplementedError("initialize_gui() is missing code")
        win.geometry(f"{res[0]}x{res[1]}-0-1")

        bttn = ctk.CTkButton(win, text="animate", command=lambda: self.explode_win())
        bttn.pack(expand=True)

        win.mainloop()

    def import_imgs(self, img_path) -> list[str]:
        img_paths= []
        for _, __, img_data in walk(img_path):
            sorted_data = sorted(
                img_data, key=lambda item: int(item.split(".")[0][-2:])
            )
            full_path_data = [img_path + "/" + i for i in sorted_data]
            for i in full_path_data:
                img_paths.append(i)

        ctk_imgs: list[str] = []
        for img in img_paths:
            frame = Image.open(img)
            resized_frm = frame.resize(self.screen_size)
            converted_frm = ImageTk.PhotoImage(resized_frm)
            ctk_imgs.append(converted_frm)

        return ctk_imgs
    
    def explode_win(self) -> None:
        self.boom = ctk.CTkToplevel()
        self.boom.title("Explosion")
        self.boom.overrideredirect(True)
        screen_px = self.screen_size
        self.boom.geometry(f"{screen_px[0]}x{screen_px[1]}-1-1")
        self.boom.wm_attributes("-transparentcolor", "white", '-topmost', 1)

        self.label = ctk.CTkLabel(self.boom, text="", fg_color="white")
        self.label.pack(expand=True, fill="both")

        x = threading.Thread(target=self.animate_explosion)
        y = threading.Thread(target=self.play_sound)
        x.start()
        y.start()

    def play_sound(self) -> None:
        mixer.init()
        mixer.Sound('minecraft-tnt-explosion.mp3').play()
        time.sleep(5)
        mixer.quit()

    def animate_explosion(self) -> None:
        if self.frm_index < self.animation_len:
            frame_label = self.label
            self.frm_index += 1

            frame_label.configure(image=self.explosion_frames[self.frm_index])
            frame_label.after(28, self.animate_explosion)

            if self.frm_index >= self.animation_len:
                self.frm_index = 2
                self.boom.destroy()


def main(**kwargs) -> int:
    menu_win = kwargs.get("menu_win")
    explode_win = kwargs.get("explode_win")

    menu_px = kwargs.get("menu_size")
    screen_px = kwargs.get("screen_size")

    instance = Bomb(explode_win, kwargs.get("frames_path"), screen_px)
    instance.initialize_gui(menu_win, menu_px)

    return 0


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    root = ctk.CTk()
    explode_win = "" # ctk.CTkToplevel()
    root.title("Bomodoro alpha")

    default_res = (1600, 900)
    menu_res = (300, 400)
    explosion_path = "./assets/explosion"

    main(menu_win=root, menu_size=menu_res, explode_win=explode_win, frames_path=explosion_path, screen_size=default_res)
