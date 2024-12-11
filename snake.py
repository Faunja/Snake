# snake.py
# By Kayden Campbell
# Copyright 2024
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 ./snake.py
import pygame, random, os
pygame.init()
DISPLAYSURF = pygame.display.get_desktop_sizes()
SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF[0]
SCREEN_HEIGHT = SCREEN_HEIGHT*3/4
cell_size = round(SCREEN_HEIGHT//10)
SCREEN_HEIGHT = SCREEN_HEIGHT//cell_size*cell_size+cell_size
screen = pygame.display.set_mode((SCREEN_HEIGHT - cell_size, SCREEN_HEIGHT))
grid_height = round((SCREEN_HEIGHT-cell_size)/cell_size)
grid = []
def set_grid():
	if len(grid) != 0:
		grid.clear()
	for row in range(grid_height):
		grid.append([0]*grid_height)
	grid[grid_height-round(grid_height/2)][grid_height-round(grid_height/2)] = 3
	apple = 0
	while apple == 0:
		x = random.randint(1, grid_height)-1
		y = random.randint(1, grid_height)-1
		if grid[x][y] == 0:
			grid[x][y] = 1
			apple = 1
def draw_grid(ended, length):
	hexed = 0
	for row in range(grid_height):
		hexed = 25 - hexed
		for col in range(grid_height):
			x = col * cell_size
			y = row * cell_size + cell_size
			rect = pygame.Rect(x, y, cell_size, cell_size)
			apple = pygame.Rect(x+cell_size*(1/6), y+cell_size*(1/6), cell_size*(2/3), cell_size*(2/3))
			if grid[row][col] < 2:
				pygame.draw.rect(screen, (90-hexed, 90-hexed, 90-hexed), rect)
				if grid[row][col] == 1:
					pygame.draw.rect(screen, (210, 0, 0), apple)
			else:
				if grid[row][col] < 6:
					pygame.draw.rect(screen, (0, 210, 0), rect)
					if grid[row][col] == 2:
						lefteye = pygame.Rect(x+cell_size*(1/8), y+cell_size*(1/16), cell_size*(1/4), cell_size*(1/4))
						righteye = pygame.Rect(x+cell_size*(5/8), y+cell_size*(1/16), cell_size*(1/4), cell_size*(1/4))
						pygame.draw.rect(screen, (0, 0, 0), lefteye)
						pygame.draw.rect(screen, (0, 0, 0), righteye)
					elif grid[row][col] == 3:
						lefteye = pygame.Rect(x+cell_size*(11/16), y+cell_size*(1/8), cell_size*(1/4), cell_size*(1/4))
						righteye = pygame.Rect(x+cell_size*(11/16), y+cell_size*(5/8), cell_size*(1/4), cell_size*(1/4))
						pygame.draw.rect(screen, (0, 0, 0), lefteye)
						pygame.draw.rect(screen, (0, 0, 0), righteye)
					elif grid[row][col] == 4:
						lefteye = pygame.Rect(x+cell_size*(1/8), y+cell_size*(11/16), cell_size*(1/4), cell_size*(1/4))
						righteye = pygame.Rect(x+cell_size*(5/8), y+cell_size*(11/16), cell_size*(1/4), cell_size*(1/4))
						pygame.draw.rect(screen, (0, 0, 0), lefteye)
						pygame.draw.rect(screen, (0, 0, 0), righteye)
					else:
						lefteye = pygame.Rect(x+cell_size*(1/16), y+cell_size*(1/8), cell_size*(1/4), cell_size*(1/4))
						righteye = pygame.Rect(x+cell_size*(1/16), y+cell_size*(5/8), cell_size*(1/4), cell_size*(1/4))
						pygame.draw.rect(screen, (0, 0, 0), lefteye)
						pygame.draw.rect(screen, (0, 0, 0), righteye)
				else:
					pygame.draw.rect(screen, (0, 210-round((grid[row][col]-20)*(150/grid_height**2)), 0), rect)
			hexed = 25 - hexed
	font = pygame.font.Font('freesansbold.ttf', cell_size)
	text = font.render("Score : "+str(length-3), True, (255, 255, 255))
	textRect = text.get_rect()
	textRect.center = (SCREEN_HEIGHT/2-cell_size/2, cell_size-cell_size/2)
	screen.blit(text, textRect)
	if ended != 0:
		font = pygame.font.Font('freesansbold.ttf', cell_size*2)
		if ended == 1:
			text = font.render('You Win!', True, (0, 255, 0), (0, 0, 0))
			textRect = text.get_rect()
		else:
			text = font.render('You Lose!', True, (255, 0, 0), (0, 0, 0))
			textRect = text.get_rect()
		textRect.center = ((SCREEN_HEIGHT-cell_size)/2, SCREEN_HEIGHT/2)
		screen.blit(text, textRect)
def update_grid(direction, length):
	apple = 0
	ended = 0
	for row in range(grid_height):
		for col in range(grid_height):
			if grid[row][col] > 20:
				grid[row][col] += 1
				if grid[row][col] > length+20:
					grid[row][col] = 0
	for row in range(grid_height):
		for col in range(grid_height):
			if grid[row][col] == 1:
				apple = 1
			elif 1 < grid[row][col] < 6:
				grid[row][col] = direction
				if grid[row][col] == 2:
					if 0 <= row-1 < grid_height and grid[row-1][col] < 2:
						grid[row-1][col] = 12
						grid[row][col] = 21
					else:
						ended = 2
				elif grid[row][col] == 3:
					if 0 <= col+1 < grid_height and grid[row][col+1] < 2:
						grid[row][col+1] = 13
						grid[row][col] = 21
					else:
						ended = 2
				elif grid[row][col] == 4:
					if 0 <= row+1 < grid_height and grid[row+1][col] < 2:
						grid[row+1][col] = 14
						grid[row][col] = 21
					else:
						ended = 2
				elif grid[row][col] == 5:
					if 0 <= col-1 < grid_height and grid[row][col-1] < 2:
						grid[row][col-1] = 15
						grid[row][col] = 21
					else:
						ended = 2
	if apple == 1:
		for row in range(grid_height):
			for col in range(grid_height):
				if 10 < grid[row][col] < 20:
					grid[row][col] -= 10
		ate = 0
	else:
		ate = 1
		empty = 0
		for row in range(grid_height):
			for col in range(grid_height):
				if 10 < grid[row][col] < 20:
					grid[row][col] -= 10
				elif grid[row][col] < 2:
					empty += 1
		if empty != 0:
			while apple == 0:
				x = random.randint(1, grid_height)-1
				y = random.randint(1, grid_height)-1
				if grid[x][y] == 0:
					grid[x][y] = 1
					apple = 1
		else:
			empty = 1
	return ate, ended
def main():
	FPS = 24
	clock = pygame.time.Clock()
	ended = 0
	move = 0
	length = 3
	direction = 0
	next_direction = [direction, 0, 0]
	reset = False
	run = True
	set_grid()
	while run:
		clock.tick(FPS)
		if reset == True:
			ended = 0
			move = 0
			length = 3
			direction = 0
			next_direction = [direction, 0, 0]
			reset = False
			set_grid()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_r:
					reset = True
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					if next_direction[0] != direction and next_direction[2] < round(FPS/6):
						next_direction[1] = 2
					else:
						if direction != 4:
							next_direction[0] = 2
					if move == 0:
						move = 1
					next_direction[2] = 0
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					if next_direction[0] != direction and next_direction[2] < round(FPS/6):
						next_direction[1] = 3
					else:
						if direction != 5:
							next_direction[0] = 3
					if move == 0:
						move = 1
					next_direction[2] = 0
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					if next_direction[0] != direction and next_direction[2] < round(FPS/6):
						next_direction[1] = 4
					else:
						if direction != 2:
							next_direction[0] = 4
					if move == 0:
						move = 1
					next_direction[2] = 0
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					if next_direction[0] != direction and next_direction[2] < round(FPS/6):
						next_direction[1] = 5
					else:
						if direction != 3:
							next_direction[0] = 5
					if move == 0:
						move = 1
					next_direction[2] = 0
			if event.type == pygame.QUIT:
				run = False
		screen.fill((0,0,0))
		if ended == 0 and move != 0:
			if move >= round(FPS/4):
				if next_direction[0] != direction:
					direction = next_direction[0]
				elif next_direction[1] != 0:
					direction = next_direction[1]
					next_direction[0] = direction
					next_direction[1] = 0
				ate, ended = update_grid(direction, length)
				if ate == 1:
					length += 1
				move = 1
			else:
				move += 1
				next_direction[2] += 1
		draw_grid(ended, length)
		pygame.display.update()
	pygame.quit()
main()
