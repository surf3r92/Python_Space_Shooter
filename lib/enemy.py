import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *

# class Enemy(pygame.sprite.Sprite):
	# def __init__(self, x, y):
		# pygame.sprite.Sprite.__init__(self)
		# self.image, self.rect = load_image("img/sprites/enemy.png", -1)
		# self.x = x
		# self.y = y
		# self.reverse = 0
		# self.frame = random.randint(0,30)
		

	
	# def update(self, dx, dy):
		# self.frame += 1
		# if self.x > 800 - self.image.get_width():
			# self.reverse = 1
		# elif self.x < 0:
			# self.reverse = 0
			
		# if self.reverse == 1:
			# dx *= -1
			# dx += 2
			
		# if self.frame < 60:
			# self.y += 3
			# self.x += (dx-3)
		# else:
			# self.x += (dx-1)
			# self.y += (dy-2)
			
		# if self.frame % 90 == 0:
			# print "enemy shoot"
			# enemyLaserSprites.append(EnemyLaser(self.x, self.y))
		

		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("img/sprites/enemy.png", -1)
		self.rect.center = pos
		self.reverse = 0
		self.counter = 0
		
	def update(self):
		self.counter +=1
		dx = random.randint(1,17)-5
		dy = random.randint(1,10)-5
		if self.rect.right > 800:
			self.reverse = 1
		if self.rect.left < 0:
			self.reverse = 0
		if self.reverse == 1:
			dx *= -1
		self.rect.move_ip(dx, dy)
		
		if self.counter%90 == 0:
			enemyLaserSprites.add(EnemyLaser(self.rect.center))
		
		
class EnemyLaser(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("img/sprites/elaser.png", -1)
		self.rect.center = pos
		

	def update(self):
		self.rect.move_ip(0,10)


global enemies
enemies = pygame.sprite.RenderPlain()		
		
global enemyLaserSprites
enemyLaserSprites = pygame.sprite.RenderPlain()