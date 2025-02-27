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
        win.geometry(f"{res[0]}x{res[1]}-0-1")

        bttn_frame = ctk.CTkFrame(win, border_width=2)
        bttn_frame.place(relx=0.5, rely=0.5, anchor='center')

        spacer0 = ctk.CTkLabel(bttn_frame, text="")
        spacer0.grid(row=0, column=0)

        timer = ctk.CTkButton(bttn_frame, text="timer", command=lambda: self.time_win())
        timer.grid(row=1, column=0, padx=20)

        spacer1 = ctk.CTkLabel(bttn_frame, text="")
        spacer1.grid(row=2, column=0)

        bttn = ctk.CTkButton(bttn_frame, text="animate", command=lambda: self.explode_win())
        bttn.grid(row=3, column=0, padx=15)

        spacer2 = ctk.CTkLabel(bttn_frame, text="")
        spacer2.grid(row=4, column=0)

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
    
    def time_win(self) -> None:
        # raise NotImplementedError("initialize_gui() is missing code")
        timer = ctk.CTkToplevel()
        timer.geometry("200x100-40-20")
        timer.configure(fg_color='black')
        timer.overrideredirect(True)
        timer.attributes('-topmost', True)
        timer.wm_attributes("-transparentcolor", "black", '-topmost', 1)

        times = ctk.CTkLabel(timer, font=("", 34))
        times.pack(expand=True)

        def countdown():
            minutes = 99
            seconds = minutes * 99
            while seconds > 0:
                mins, secs = divmod(seconds, 99)
                times.configure(text='{:02d}:{:02d}'.format(mins, secs))
                timer.update()
                time.sleep(1)
                seconds -= 1
            timer.destroy()
            self.explode_win()

        countdown()
    
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
        mixer.Sound('assets/sounds/minecraft-tnt-explosion.mp3').play()
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
