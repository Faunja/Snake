# definegrid.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *

class definegrid:
	def __init__(self):
		self.width = 20
		self.height = round(ScreenHeight / ScreenWidth * self.width)
		self.cellSize = ScreenWidth / self.width
		self.grid = []
		for column in range(self.height):
			self.grid.append([0] * self.width)

Grid = definegrid()