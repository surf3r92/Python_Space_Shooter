import os, sys, pygame, random, math
import numpy as np
from pygame.locals import *
from lib.methods import *

		
class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image("img/sprites/enemy.png", -1)
		self.rect.center = pos
		if pos[0] > 400:
			self.reverse = 1
		else:
			self.reverse = 0
		self.counter = 50
		self.xList = np.linspace(np.pi,np.pi*3,100)
		self.yList = np.sin(self.xList)
		print self.xList
		print self.yList
	# def update(self):
		# self.counter +=1
		# dx = random.randint(1,17)-5
		# dy = random.randint(1,10)-5
		# if self.rect.right > 800:
			# self.reverse = 1
		# if self.rect.left < 0:
			# self.reverse = 0
		# if self.reverse == 1:
			# dx *= -1
		# self.rect.move_ip(dx, dy)
		
		# if self.counter%90 == 0:
			# enemyLaserSprites.add(EnemyLaser(self.rect.center))
			
	def update(self):
		self.counter += 1
		if self.counter > 100:
			
			dx = 5
			dy = self.yList[self.counter%100]
			if self.rect.right > 800:
				self.reverse = 1
			if self.rect.left < 0:
				self.reverse = 0
			if self.reverse == 1:
				dx *= -1
			self.rect.move_ip(dx,dy*6)
			
		else:
			self.xStart = np.linspace(0,np.pi,50)
			self.yStart = np.sin(self.xStart)
			dx = 5
			dy = self.yStart[self.counter%50]
			if self.reverse == 1:
				dx *= -1
			self.rect.move_ip(dx,dy*8)
			print "xstart"
			print self.xStart
			print "yStart"
			print self.yStart
			print "xList"
			print self.xList
			print "yList"
			print self.yList
	
	# def cosineInterpolation(y1, y2, mu):
		# mu2 = (1-cos(mu*PI))/2
		# return (y1*(1-mu2)+y2*mu2);
		
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