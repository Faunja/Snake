# variables.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame

pygame.init()
DISPLAYSURF = pygame.display.get_desktop_sizes()
ScreenWidth, ScreenHeight = DISPLAYSURF[0]
SizeDifference = 3/4
ScreenWidth = round(ScreenHeight * SizeDifference)
ScreenHeight = round(ScreenHeight * SizeDifference)
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

Black = (0, 0, 0)
Red = (255, 60, 60)
Green = (60, 255, 60)
Blue = (60, 60, 255)
White = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()
