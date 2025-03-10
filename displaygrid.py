# displaygrid.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
from variables import *
from definegrid import Grid
from defineuser import User

def draw_head(xPosition, yPosition):
	size = (Grid.cellSize / 10, Grid.cellSize * (9 / 10))

	topRight = (xPosition + size[0], yPosition + size[0])
	bottomRight = (xPosition + size[0], yPosition + size[1])
	bottomLeft = (xPosition + size[1], yPosition + size[1])
	topLeft = (xPosition + size[1], yPosition + size[0])

	return (topRight, bottomRight, bottomLeft, topLeft)

def draw_segment(xPosition, yPosition, direction):
	size = (Grid.cellSize / 10, Grid.cellSize * (9 / 10))
	adjustSize = (direction[0][0] * Grid.cellSize, direction[0][1] * Grid.cellSize, direction[1][0] * Grid.cellSize, direction[1][1] * Grid.cellSize)

	topRight = (xPosition + size[1] + adjustSize[1], yPosition + size[0] - adjustSize[2])
	bottomRight = (xPosition + size[1] + adjustSize[1], yPosition + size[1] + adjustSize[3])
	bottomLeft = (xPosition + size[0] - adjustSize[0], yPosition + size[1] + adjustSize[3])
	topLeft = (xPosition + size[0] - adjustSize[0], yPosition + size[0] - adjustSize[2])

	return (topRight, bottomRight, bottomLeft, topLeft)

def display_player():
	headX = User.position[0] * Grid.cellSize
	headY = User.position[1] * Grid.cellSize + HeightDifference
	pygame.draw.polygon(screen, Blue, draw_head(headX, headY))
	for segment in User.tail:
		segmentX = segment.position[0] * Grid.cellSize
		segmentY = segment.position[1] * Grid.cellSize + HeightDifference
		pygame.draw.polygon(screen, Blue, draw_segment(segmentX, segmentY, segment.display_directions()))

def draw_apple(xPosition, yPosition):
	size = (Grid.cellSize / 4, Grid.cellSize * (3 / 4))

	topRight = (xPosition + size[0], yPosition + size[0])
	bottomRight = (xPosition + size[0], yPosition + size[1])
	bottomLeft = (xPosition + size[1], yPosition + size[1])
	topLeft = (xPosition + size[1], yPosition + size[0])

	return (topRight, bottomRight, bottomLeft, topLeft)

def display_apple():
	for apple in Grid.apples:
		appleX = apple.position[0] * Grid.cellSize
		appleY = apple.position[1] * Grid.cellSize + HeightDifference
		pygame.draw.polygon(screen, Yellow, draw_apple(appleX, appleY))
