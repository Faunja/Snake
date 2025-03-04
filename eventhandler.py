# eventhandler.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineuser import User
from definegrid import Grid

def key_events(event):
	if event.key == pygame.K_ESCAPE:
		User.playing = False
	if event.key == pygame.K_f:
		User.change_showfps()

def search_events():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			key_events(event)
		if event.type == pygame.QUIT:
			User.playing = False