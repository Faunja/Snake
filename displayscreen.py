# displayscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from displaygrid import display_player, display_apple
from displaytext import display_text

def show_mouseposition():
	mouseX, mouseY = pygame.mouse.get_pos()
	xPosition = mouseX // Grid.cellSize * Grid.cellSize
	yPosition = mouseY // Grid.cellSize * Grid.cellSize
	rect = pygame.Rect(xPosition, yPosition, Grid.cellSize, Grid.cellSize)
	pygame.draw.rect(screen, White, rect)

def display_background():
	screen.fill(Black)
	display_apple()
	display_player()
	pygame.draw.rect(screen, White, (0, HeightDifference - 10, ScreenWidth, 10))
	display_text()
