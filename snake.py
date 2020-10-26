import pygame 
import sys
import copy
import random
import time

pygame.init()


width=500
height=500
scale=10
score=0

food_x=10
food_y=10

display=pygame.display.set_mode((width,height))
pygame.display.set_caption("snake game")
clock = pygame.time.clock()

background = (23,32,42)
snake_color = (236,240,241)
food_color = (148,49,38)
snake_head = (247,220,111)


class snake:
	"""docstring for snake"""
	def __init__(self, x_start, y_start):
		self.x = x_start
		self.y = y_start
		self.w = 10
		self.h = 10
		self.x_dir = 1
		self.y_dir = 0
		self.history = [[self.x,self.y]]
		self.length = 1
		




