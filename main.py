# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineuser import User
from eventhandler import search_events
from background import display_background
from text import display_text

def main():
	while User.playing:
		clock.tick(FPS)
		search_events()
		display_background()
		display_text()
		pygame.display.update()
	pygame.quit()

main()