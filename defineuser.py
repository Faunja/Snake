# defineuser.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
from variables import *

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

	def display_directions(self):
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
		self.tailSize = 3
		self.tail = []

	def change_showfps(self):
		self.showfps = change_TrueFalse(self.showfps)
	
	def change_direction(self, x, y):
		self.direction = (x, y)
	
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
		self.adjust_tail()
		self.shift_position()

User = defineuser()
