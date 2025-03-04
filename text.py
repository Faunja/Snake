# text.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineuser import User

defaultFont = 'Fonts/m6x11.ttf'
fontColor = White

def draw_text(text, position, centered = True):
	font = pygame.font.Font(defaultFont, round(ScreenHeight / 32))
	printed = font.render(text, True, fontColor)
	printed_width, printed_height = printed.get_size()
	if centered == True:
		screen.blit(printed, (position[0] - printed_width / 2, position[1] - printed_height / 2))
		return
	screen.blit(printed, (position[0], position[1]))
	

def display_fps():
	draw_text(f'{clock.get_fps() :.1f}', (0, 0), False)

def display_text():
	if User.showfps == True:
		display_fps()