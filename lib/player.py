import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/ship.png", -1)
        self.rect.center = (400, 500)
        self.dx = 0
        self.dy = 0
        self.laserTimer = 0
        self.laserMax = 5
        self.reset()

    def update(self):
        self.rect.move_ip((self.dx, self.dy))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.laserTimer += 1
            if self.laserTimer == self.laserMax:
                laserSprites.add(Laser(self.rect.midtop))
                self.laserTimer = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 260:
            self.rect.top = 260
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

    def reset(self):
        self.rect.bottom = 600


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/laser.png", -1)
        self.rect.center = pos

    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:
            self.rect.move_ip(0, -15)


global laserSprites
laserSprites = pygame.sprite.RenderPlain()