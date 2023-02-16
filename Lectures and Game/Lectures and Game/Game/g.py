import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import random

#Constants for the game
WIDTH, HEIGHT = (32, 32)
black=(0,0,0)
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # RED
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)
NONE = (0,0)
count=0

blue=pygame.image.load('blue.png')
blue=pygame.transform.scale(blue,(32,32))
wall=pygame.image.load('wall1.png')
wall=pygame.transform.scale(wall,(32,32))
pacman=pygame.image.load('yo.png')
pacman=pygame.transform.scale(pacman,(32,32))
coin=pygame.image.load('coin.png')
coin=pygame.transform.scale(coin,(32,32))

def count_time(seconds,minutes):
	font=pygame.font.SysFont(None,50)
	seconds="Time = " + str(minutes) + ' : ' + str(seconds)
	text=font.render(seconds ,True,black)
	screen.blit(text,(350,0))

def Lives_disp(count):
	font=pygame.font.SysFont(None,40)
	text=font.render(" Lives - " + str(count),True,black)
	screen.blit(text,(200,0))

def add_enemy(screen,enm):
	i=random.randint(1,4)
	a=pixels_from_points(enm)
	
	screen.blit(blue,a)
	

def enemy(pos,layout):
	switch=random.randint(1,10)
	
	duck=True
	while duck :
		switch=random.randint(1,10)
		if switch==1 or switch==3 or switch ==5:
			enemy_pos=add_to_pos(pos,LEFT)
		elif switch==2 or switch==4 or switch==6:
			enemy_pos=add_to_pos(pos,RIGHT)
		elif switch==7 or switch ==8:
			enemy_pos=add_to_pos(pos,TOP)
		else:
			enemy_pos=add_to_pos(pos,DOWN)

		if obstacle(enemy_pos,layout):
			duck=False

	return enemy_pos


def score(count):
	font=pygame.font.SysFont(None,25)
	text=font.render(" Points - " + str(count),True,black)
	screen.blit(text,(0,0))

def level_message():
	font=pygame.font.SysFont(None,50)
	text=font.render(" LEVEL COMPLETE ",True,black)
	screen.blit(text,(153,300))


def crash_message():
	font=pygame.font.SysFont(None,50)
	text=font.render(" CRASHED ",True,black)
	screen.blit(text,(153,300))

def coin_collection(new_pos,layout):
	
	if layout[new_pos[1]][new_pos[0]]=="c":
		
		layout[new_pos[1]][new_pos[0]]="."
		return True

	else:
		return False
		

		


def obstacle(new_pos,layout):
	
	if layout[new_pos[1]][new_pos[0]]=="w":
		return False
	else:
		return True


#Draws a rectangle for the wall
def draw_wall(screen, pos):
	
	pixels = pixels_from_points(pos)
	screen.blit(wall,pixels)
	# pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the player
def draw_pacman(screen, pos): 

	pixels = pixels_from_points(pos)
	screen.blit(pacman,pixels)
	
	# pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])

#Draws a rectangle for the coin
def draw_coin(screen, pos):

	pixels = pixels_from_points(pos)
	screen.blit(coin,pixels)
	# pygame.draw.rect(screen, COIN_COLOR, [pixels, (WIDTH, HEIGHT)])

#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((640,640), 0, 32)
background = pygame.surface.Surface((640,640)).convert()


#Initializing variables
layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
background.fill((0,0,0))

enemy1=(6,8)
enemy2=(17,1)
enemy3=(4,14)
enemy4=(16,18)


crash=False

# Main game loop 
x_sec=0

lives=3

seconds=0
minutes=0

count = 0
while crash is False:
	
	

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()


		#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
		# Pacman Movements....Keydown and keyup movements accordingly.
		# Special Key - TAB to STop pacman..


	screen.blit(background, (0,0))


	#Draw board from the 2d layout array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos)

	#Draw the player
	draw_pacman(screen, pacman_position)

	add_enemy(screen,enemy1)
	add_enemy(screen,enemy2)
	add_enemy(screen,enemy3)
	add_enemy(screen,enemy4)
	
	enemy1=enemy(enemy1,layout)
	enemy2=enemy(enemy2,layout)
	enemy3=enemy(enemy3,layout)
	enemy4=enemy(enemy4,layout)

	
	move_direction = NONE

#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
# Pacman Movements....Keydown and keyup movements accordingly.
# Special Key - TAB to STop pacman..


	if event.type==pygame.KEYDOWN:


		if event.key==pygame.K_LEFT:
			new_pos = add_to_pos(pacman_position, LEFT)
			
			if obstacle(new_pos,layout):
				move_direction=LEFT


		
		elif event.key==pygame.K_RIGHT:
			new_pos = add_to_pos(pacman_position, RIGHT)
			
			if obstacle(new_pos,layout):
				move_direction=RIGHT
			
		
		elif event.key==pygame.K_UP:
			new_pos = add_to_pos(pacman_position, TOP)
			
			if obstacle(new_pos,layout):
				move_direction=TOP
		
	
		elif event.key==pygame.K_DOWN:
			new_pos = add_to_pos(pacman_position, DOWN)
			
			if obstacle(new_pos,layout):
				move_direction=DOWN
				

		elif event.key==pygame.K_TAB:
			new_pos = add_to_pos(pacman_position, NONE)
			




	if event.type==pygame.KEYUP:
		if event.key==pygame.K_RIGHT :
			
			new_pos = add_to_pos(pacman_position, RIGHT)
		
			if obstacle(new_pos,layout)==1:
				move_direction=RIGHT

		elif event.key==pygame.K_LEFT:
			
			new_pos = add_to_pos(pacman_position, LEFT)
			
			if obstacle(new_pos,layout)==1:
				move_direction=LEFT

		elif event.key==pygame.K_UP:

			new_pos = add_to_pos(pacman_position, TOP)
			
			if obstacle(new_pos,layout)==1:
				move_direction=TOP

		elif event.key==pygame.K_DOWN:

			new_pos = add_to_pos(pacman_position, DOWN)
			
			if obstacle(new_pos,layout)==1:
				move_direction=DOWN

	#Update player position based on movement.
	if coin_collection(pacman_position,layout):
		count=count+1

	score(count)

	if count==28:
		level_message()


	pacman_position = add_to_pos(pacman_position, move_direction)

	Lives_disp(lives)
	if enemy1==pacman_position or enemy2==pacman_position or enemy3==pacman_position or enemy4==pacman_position :
		lives=lives-1
		Lives_disp(lives)
		pacman_position=(1,1)
		crash_message()
		# crash=True


	if lives==0:

		crash=True


	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array

	#Update the display

	x_sec=x_sec+1
	if x_sec%10==0:
		seconds=seconds+1
	if seconds==60:
		seconds=0
		minutes=minutes+1

	count_time(seconds,minutes)

	pygame.display.update()

	#Wait for a while, computers are very fast.
	time.sleep(0.1)