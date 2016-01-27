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
        self.invincible = 1

        self.special = 0
        self.dxMid = 0
        self.dyMid = 0
        self.midCounter = 0

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
            self.invincible = 0
            if self.special == 1:
                self.midCounter += 1
                self.rect.move_ip(self.dxMid, self.dyMid)
                if self.midCounter == 30:
                    for i in range(0, 16):
                        bossLaserSprites.add(BossLaser(self.rect.center, i-8))
                        self.special = 0
                        self.midCounter = 0

            else:
                self.rect.move_ip(dx*random.randint(1, 2), random.randint(0, 1))
                if self.counter % 45 == 0:

                    bossLaserSprites.add(BossLaser(self.rect.center, random.randint(-3, 3)))
                elif self.counter % 33 == 0:
                    bossLaserSprites.add(BossLaser(self.rect.center, random.randint(-3, 3)))
                elif self.counter % 333 == 0:
                    self.special = 1
                    self.dxMid = (400 - self.rect.center[0])/30
                    self.dyMid = (100 - self.rect.center[1])/30

        else:
            self.rect.move_ip(0, 2)


class BossLaser(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/elaser.png", -1)
        self.rect.center = pos
        self.direction = direction

    def update(self):
        self.rect.move_ip(self.direction, 10)
        if self.rect.bottom > 540:
            self.kill()


global bossLaserSprites
bossLaserSprites = pygame.sprite.RenderPlain()
global boss
boss = pygame.sprite.RenderPlain()
