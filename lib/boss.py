import os, sys, pygame, random, math
import numpy as np
from pygame.locals import *
from lib.methods import *


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/boss.png", -1)
        self.rect.center = pos


    def update(self):
        self.counter += 1
        if self.counter > 100:
            #add boss movement pattern
            pass
        else:
            #add boss pattern to enter screen
            pass

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