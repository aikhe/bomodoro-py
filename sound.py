from pygame import mixer
import time

mixer.init()
sound = mixer.Sound('minecraft-tnt-explosion.mp3')
sound.play()

time.sleep(5)

mixer.quit()