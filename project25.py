# This is coding for making a projec on healthy programmer

import pygame
import time

pygame.mixer
pygame.mixer.init()


pygame.mixer.music.load("aroma.mp3")  

pygame.mixer.music.set_volume(1.0)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)