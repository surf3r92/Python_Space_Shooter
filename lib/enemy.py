import os, sys, pygame, random, math
import numpy as np
from pygame.locals import *
from lib.methods import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/enemy.png", -1)
        self.pos = pos
        self.rect.center = self.pos
        if self.pos[0] <= 100 or self.pos[0] >= 700:
            self.side = 1
        else:
            self.side = 0
        if self.pos[0] == 400:
            self.reverse = random.randint(0, 1)
        elif self.pos[0] > 400:
            self.reverse = 1
        elif self.pos[0] < 400:
            self.reverse = 0

        if self.pos[0] <= 100 or self.pos[0] >= 700:
            self.xStart = np.linspace(np.pi, np.pi*2, 50)
            self.yStart = np.sin(self.xStart)
            for elem in self.yStart:
                elem += 1
        else:
            self.xStart = np.linspace(0, np.pi, 50)
            self.yStart = np.sin(self.xStart)


        self.counter = 50
        self.factor = random.randint(2, 7)
        self.xList = np.linspace(np.pi, np.pi * 3, 100)
        self.yList = np.sin(self.xList)
        self.dx = random.randint(4, 6)

    def update(self):
        if self.side == 1:
            self.counter += 50
            self.side = 0

        self.counter += 1
        if self.counter > 100:
            dx = self.dx
            dy = self.yList[self.counter % 100]
            if self.rect.right > 800:
                self.reverse = 1
            if self.rect.left < 0:
                self.reverse = 0
            if self.reverse == 1:
                dx *= -1
            self.rect.move_ip(dx, dy * self.factor)

            if self.counter % 75 == 0:
                enemyLaserSprites.add(EnemyLaser(self.rect.center))


        else:
            dx = 5
            dy = self.yStart[self.counter % 50]
            if self.reverse == 1:
                dx *= -1
            self.rect.move_ip(dx, dy * 9)


class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/elaser.png", -1)
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 540:
            self.kill()

class Meteorite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/meteorite.png", -1)
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 540:
            self.kill()

global enemyLaserSprites
enemyLaserSprites = pygame.sprite.RenderPlain()
global enemies
enemies = pygame.sprite.RenderPlain()
global meteorites
meteorites = pygame.sprite.RenderPlain()