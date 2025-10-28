# Exercise 006: Modules
# create a program to ready a file music (.mp3)

import pygame
from os import path

pygame.init()

base_path = path.dirname(__file__)  
music_path = path.join(base_path, "../../assets/audio/movies.mp3")

pygame.mixer.music.load(path.abspath(music_path))

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
