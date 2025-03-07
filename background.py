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

def show_head(xPosition, yPosition):
	size = (Grid.cellSize / 10, Grid.cellSize * (9 / 10))

	topRight = (xPosition + size[0], yPosition + size[0])
	bottomRight = (xPosition + size[0], yPosition + size[1])
	bottomLeft = (xPosition + size[1], yPosition + size[1])
	topLeft = (xPosition + size[1], yPosition + size[0])

	return (topRight, bottomRight, bottomLeft, topLeft)

def show_segment(xPosition, yPosition, direction):
	size = (Grid.cellSize / 10, Grid.cellSize * (9 / 10))
	adjustSize = (direction[0][0] * Grid.cellSize, direction[0][1] * Grid.cellSize, direction[1][0] * Grid.cellSize, direction[1][1] * Grid.cellSize)

	topRight = (xPosition + size[1] + adjustSize[1], yPosition + size[0] - adjustSize[2])
	bottomRight = (xPosition + size[1] + adjustSize[1], yPosition + size[1] + adjustSize[3])
	bottomLeft = (xPosition + size[0] - adjustSize[0], yPosition + size[1] + adjustSize[3])
	topLeft = (xPosition + size[0] - adjustSize[0], yPosition + size[0] - adjustSize[2])

	return (topRight, bottomRight, bottomLeft, topLeft)

def show_player():
	headX = User.position[0] * Grid.cellSize
	headY = User.position[1] * Grid.cellSize
	pygame.draw.polygon(screen, Blue, show_head(headX, headY))
	for segment in User.tail:
		segmentX = segment.position[0] * Grid.cellSize
		segmentY = segment.position[1] * Grid.cellSize
		pygame.draw.polygon(screen, Blue, show_segment(segmentX, segmentY, segment.give_direction()))

def display_background():
	screen.fill(Black)
	show_player()
	
