# defineuser.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *

class defineuser:
	def __init__(self):
		self.playing = True
		self.showfps = False

	def change_showfps(self):
		if self.showfps == False:
			self.showfps = True
			return
		self.showfps = False

User = defineuser()