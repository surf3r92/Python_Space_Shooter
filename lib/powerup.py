import os, sys, pygame, random, math
import numpy as np
from pygame.locals import *
from lib.methods import *


class Powerup(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        if type == "fasterLaser":
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image("img/sprites/powerup_faster_shoot.png", -1)
            self.rect.center = pos
        elif type == "health":
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image("img/sprites/powerup_heart.png", -1)
            self.rect.center = pos
        elif type == "damage":
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image("img/sprites/power_up_double_shoot.png", -1)
            self.rect.center = pos
        elif type == "shield":
            pygame.sprite.Sprite.__init__(self)
            self.image, self.rect = load_image("img/sprites/powerup_shield.png", -1)
            self.rect.center = pos

    def update(self):
        if self.rect.bottom > 540:
            self.kill()
        else:
            self.rect.move_ip(0, 5)


global laserPowerups
laserPowerups = pygame.sprite.RenderPlain()
