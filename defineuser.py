# defineuser.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
from variables import *
from definegrid import Grid

def change_TrueFalse(variable):
	if variable == False:
		return True
	return False

class definetail:
	def __init__(self, x, y, direction):
		self.position = (x, y)
		self.direction = direction
	
	def update_tail(self, x, y, direction):
		self.position = (x, y)
		self.direction = direction

	def give_direction(self):
		if self.direction == (1, 0):
			return ((0, 1), (0, 0))
		elif self.direction == (-1, 0):
			return ((1, 0), (0, 0))
		elif self.direction == (0, 1):
			return ((0, 0), (0, 1))
		elif self.direction == (0, -1):
			return ((0, 0), (1, 0))

class defineuser:
	def __init__(self):
		self.playing = True
		self.showfps = False
		
		self.position = [0, 0]
		self.direction = (1, 0)
		
		self.score = 0
		self.tailSize = 15
		self.tail = []
		
		self.speed = 6
		self.time = 1

	def change_showfps(self):
		self.showfps = change_TrueFalse(self.showfps)
	
	def change_direction(self, x, y):
		self.direction = (x, y)
	
	def check_wall_collision(self):
		if 0 <= self.position[0] + self.direction[0] <= Grid.width - 1 and 0 <= self.position[1] + self.direction[1] <= Grid.height - 1:
			return False
		return True
	
	def check_tail_collision(self):
		for segment in self.tail:
			if self.position[0] + self.direction[0] == segment.position[0] + segment.direction[0] and self.position[1] + self.direction[1] == segment.position[1] + segment.direction[1]:
				return True
		return False
	
	def adjust_tail(self):
		for currentTail in range(len(self.tail) - 1, -1, -1):
			if len(self.tail) < self.tailSize + self.score:
				self.tail.append(definetail(self.tail[currentTail].position[0], self.tail[currentTail].position[1], self.tail[currentTail].direction))
			if currentTail != 0:
				nextTail = self.tail[currentTail - 1]
				self.tail[currentTail].update_tail(nextTail.position[0], nextTail.position[1], nextTail.direction)
				continue
			self.tail[currentTail].update_tail(self.position[0], self.position[1], self.direction)
		if len(self.tail) == 0:
			self.tail.append(definetail(self.position[0], self.position[1], self.direction))
	
	def shift_position(self):
		self.position[0] += self.direction[0]
		self.position[1] += self.direction[1]
	
	def movement(self):
		if self.check_wall_collision() == True or self.check_tail_collision() == True:
			return
		self.adjust_tail()
		self.shift_position()

	def check_movement(self):
		if self.time >= FPS / self.speed:
			self.time = 1
			self.movement()
			return
		self.time += 1

User = defineuser()
