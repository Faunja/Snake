# definegrid.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import random
from variables import *
from defineuser import User

class defineapple:
	def __init__(self, x, y):
		self.position = (x, y)
		self.point = 1

class definegrid:
	def set_grid(self):
		self.width = 20
		self.height = round((ScreenHeight * informationSize) / ScreenWidth * self.width)
		self.cellSize = ScreenWidth / self.width

		self.maxApples = 1
		self.apples = []

		self.speed = 4
		self.time = 1
		
	def __init__(self):
		self.set_grid()
	
	def create_apple(self):
		checkPosition = True
		while checkPosition:
			xPosition = random.randrange(self.width)
			yPosition = random.randrange(self.height)
			hitSegment = False
			for segment in User.tail:
				if xPosition == segment.position[0] and yPosition == segment.position[1]:
					hitSegment = True
					break
			hitApple = False
			for apple in self.apples:
				if xPosition == apple.position[0] and yPosition == apple.position[1]:
					hitApple = True
					break
			if hitSegment == True or hitApple == True:
				continue
			if xPosition == User.position[0] and yPosition == User.position[1]:
				continue
			checkPosition = False
		self.apples.append(defineapple(xPosition, yPosition))

	def check_apples(self):
		for apple in self.apples:
			if apple.position[0] == User.position[0] and apple.position[1] == User.position[1]:
				User.score += 1
				self.apples.remove(apple)

	def check_wall_collision(self):
		if 0 <= User.position[0] + User.direction[0] <= self.width - 1 and 0 <= User.position[1] + User.direction[1] <= self.height - 1:
			return False
		return True

	def check_tail_collision(self):
		for segment in User.tail:
			if User.position[0] + User.direction[0] == segment.position[0] + segment.direction[0] and User.position[1] + User.direction[1] == segment.position[1] + segment.direction[1]:
				return True
		return False

	def game_over(self):
		if self.check_wall_collision() == True or self.check_tail_collision() == True:
			User.lose = True
			return
		User.movement()
	
	def game_win(self):
		if User.tailSize + User.score + 1 == self.width * self.height:
			User.win = True
			self.maxApples = 0
	
	def check_grid_events(self):
		if User.lose == True or User.win == True:
			return
		if self.time >= FPS / self.speed:
			User.direction = User.newDirection
			self.game_over()
			self.game_win()
			self.check_apples()
			if self.maxApples != len(self.apples):
				self.create_apple()
			self.time = 1
		self.time += 1

Grid = definegrid()
