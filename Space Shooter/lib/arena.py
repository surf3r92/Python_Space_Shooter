import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *

class Arena (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/arena.jpg", -1)
        self.dy = 3
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1200:
            self.reset()

    def reset(self):
        self.rect.top = -600