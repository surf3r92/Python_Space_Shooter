import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("img/sprites/enemy.png", -1)
		self.x = x
		self.y = y
		self.reverse = 0
		self.frame = random.randint(0,30)
		

	
	def update(self, dx, dy):
		self.frame += 1
		if self.x > 800 - self.image.get_width():
			self.reverse = 1
		elif self.x < 0:
			self.reverse = 0
			
		if self.reverse == 1:
			dx *= -1
			dx += 2
			
		if self.frame < 60:
			self.y += 3
			self.x += (dx-3)
		else:
			self.x += (dx-1)
			self.y += (dy-2)
		