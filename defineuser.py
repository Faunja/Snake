# defineuser.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from definegrid import Grid

def change_TrueFalse(variable):
	if variable == False:
		return True
	return False

class definetail:
	def __init__(self, x, y, frontDirection, backDirection = False):
		self.position = (x, y)
		self.frontDirection = frontDirection
		self.backDirection = backDirection
	
	def update_tail(self, x, y, newDirection):
		self.position = (x, y)
		self.backDirection = self.frontDirection
		self.frontDirection = newDirection

class defineuser:
	def __init__(self):
		self.playing = True
		self.showfps = False
		
		self.position = [0, 0]
		self.direction = (1, 0)
		self.newDirection = (1, 0)
		
		self.points = 0
		self.tail = []
		
		self.speed = 4
		self.time = 1

	def change_showfps(self):
		self.showfps = change_TrueFalse(self.showfps)
	
	def check_wall_collision(self):
		if 0 <= self.position[0] + self.direction[0] <= Grid.width - 1 and 0 <= self.position[1] + self.direction[1] <= Grid.height - 1:
			return False
		return True
	
	def change_direction(self, x, y):
		self.newDirection = (x, y)
	
	def shift_position(self):
		self.direction = self.newDirection
		if self.check_wall_collision() == True:
			return
		self.position[0] += self.direction[0]
		self.position[1] += self.direction[1]
	
	def check_tail(self):
		if len(self.tail) == 0:
			self.tail.append(definetail(self.position[0], self.position[1], self.direction))
			return
		for segment in range(len(self.tail)):
			if segment == len(self.tail) - 1:
				self.tail[segment].update_tail(self.position[0], self.position[1], self.newDirection)
	
	def check_movement(self):
		if self.time >= FPS / self.speed:
			self.time = 1
			self.check_tail()
			self.shift_position()
			return
		self.time += 1

User = defineuser()
