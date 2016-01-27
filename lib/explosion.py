import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("img/sprites/Blue Explosion/1.png", -1)
        self.rect.center = pos

    def update(self, pos):
        self.rect.center = pos


def changeImage(currentExplosionImage, explosionSprite):
    explosionSprite.sprites()[0].image, explosionSprite.sprites()[0].rect = currentExplosionImage