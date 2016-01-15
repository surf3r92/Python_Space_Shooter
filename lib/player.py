import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *
from lib.enemy import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/ship.png", -1)
        self.rect.center = (400, 500)
        self.dx = 0
        self.dy = 0
        self.laserTimer = 0
        self.laserMax = 20
        self.reset()

    def update(self, damage):
        global laserSprites
        self.rect.move_ip((self.dx, self.dy))
        key = pygame.key.get_pressed()
        self.laserTimer += 1
        if key[pygame.K_SPACE]:
            if self.laserTimer > self.laserMax:
                if damage == 1:
                    laserSprites.add(Laser(self.rect.midtop))
                    self.laserTimer = 0
                elif damage == 2:
                    laserSprites.add(Laser((self.rect.left+5, self.rect.top)))
                    laserSprites.add(Laser((self.rect.right-5, self.rect.top)))
                    self.laserTimer = 0
                elif damage >= 3:
                    laserSprites.add(Laser((self.rect.left+5, self.rect.top)))
                    laserSprites.add(Laser((self.rect.right-5, self.rect.top)))
                    laserSprites.add(Laser(self.rect.midtop))
                    self.laserTimer = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 160:
            self.rect.top = 160
        elif self.rect.bottom >= 600 - 64:
            self.rect.bottom = 600 - 64

    def reset(self):
        self.rect.bottom = 600 - 64


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/laser.png", -1)
        self.rect.center = pos

    def update(self, laserSpeed):
        if self.rect.top < 0:
            self.kill()
        else:
            self.rect.move_ip(0, laserSpeed)

            # enemies_hit_list = pygame.sprite.spritecollide(self, enemies, True, self.kill())
            # try:
            # print enemies_hit_list[0]
            # except:
            # pass


global laserSprites
laserSprites = pygame.sprite.RenderPlain()

