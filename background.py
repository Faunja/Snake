# displayscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from definegrid import Grid

def check_mouseposition(xPosition, yPosition, cellSize):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if mouse_x < xPosition or mouse_x > xPosition + cellSize:
		return False
	if mouse_y < yPosition or mouse_y > yPosition + cellSize:
		return False
	return True

def draw_grid():
	for column in range(Grid.height):
		yPosition = column * Grid.cellSize
		for row in range(Grid.width):
			xPosition = row * Grid.cellSize
			if check_mouseposition(xPosition, yPosition, Grid.cellSize):
				rect = pygame.Rect(xPosition, yPosition, Grid.cellSize, Grid.cellSize)
				pygame.draw.rect(screen, White, rect)
	
def display_background():
	screen.fill(Black)
	draw_grid()