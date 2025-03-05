# displayscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from definegrid import Grid
from defineuser import User

def show_mouseposition():
	mouseX, mouseY = pygame.mouse.get_pos()
	xPosition = mouseX // Grid.cellSize * Grid.cellSize
	yPosition = mouseY // Grid.cellSize * Grid.cellSize
	rect = pygame.Rect(xPosition, yPosition, Grid.cellSize, Grid.cellSize)
	pygame.draw.rect(screen, White, rect)

def show_snakepart(xPosition, yPosition, direction):
	size = (Grid.cellSize / 10, Grid.cellSize * (9 / 10))
	if direction == (0, -1):
		topRight = (xPosition + size[0], yPosition + size[0])
		bottomRight = (xPosition + size[0], yPosition + Grid.cellSize)
		bottomLeft = (xPosition + size[1], yPosition + Grid.cellSize)
		topLeft = (xPosition + size[1], yPosition + size[0])
	if direction == (1, 0):
		topRight = (xPosition + size[0], yPosition + size[0])
		bottomRight = (xPosition + size[0], yPosition + size[1])
		bottomLeft = (xPosition + Grid.cellSize, yPosition + size[1])
		topLeft = (xPosition + Grid.cellSize, yPosition + size[0])
	if direction == (0, 1):
		topRight = (xPosition + size[0], yPosition)
		bottomRight = (xPosition + size[0], yPosition + size[1])
		bottomLeft = (xPosition + size[1], yPosition + size[1])
		topLeft = (xPosition + size[1], yPosition)
	if direction == (-1, 0):
		topRight = (xPosition, yPosition + size[0])
		bottomRight = (xPosition, yPosition + size[1])
		bottomLeft = (xPosition + size[1], yPosition + size[1])
		topLeft = (xPosition + size[1], yPosition + size[0])
		
	return (topRight, bottomRight, bottomLeft, topLeft)

def show_player():
	headX = User.position[0] * Grid.cellSize
	headY = User.position[1] * Grid.cellSize
	pygame.draw.polygon(screen, Blue, show_snakepart(headX, headY, User.direction))
	for segment in User.tail:
		segmentX = segment.position[0] * Grid.cellSize
		segmentY = segment.position[1] * Grid.cellSize
		pygame.draw.polygon(screen, Blue, show_snakepart(headX, headY, segment.frontDirection))
		if segment.backDirection != False:
			pygame.draw.polygon(screen, Blue, show_snakepart(headX, headY, segment.backDirection))

def display_background():
	screen.fill(Black)
	show_player()
	
