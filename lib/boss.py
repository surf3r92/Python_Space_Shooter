import os, sys, pygame, random, math
import numpy as np
from pygame.locals import *
from lib.methods import *



class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/boss.png", -1)
        self.rect.center = pos
        self.counter = 0
        self.health = 20
        self.reverse = 0

    def update(self):
        self.counter += 1
        dx = 5

        if self.rect.right > 800:
            self.reverse = 1
        if self.rect.left < 0:
            self.reverse = 0
        if self.reverse == 1:
            dx *= -1
        if self.counter > 100:
            self.rect.move_ip(dx,0)
        else:
            self.rect.move_ip(0,2)


class BossLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/bosslaser.png", -1)
        self.rect.center = pos

    def update(self):
        self.rect.move_ip(0, 10)


global bossLaserSprites
bossLaserSprites = pygame.sprite.RenderPlain()
global boss
boss = pygame.sprite.RenderPlain()
