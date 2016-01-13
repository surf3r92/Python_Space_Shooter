import os, sys, pygame, random
from pygame.locals import *
from lib.menu import *


def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def keyControls(self, player):
    for event in pygame.event.get():
        keystate = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            keepgoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # keepgoing = False
                self.gameState = "Pause"
                gameMenu(self)
            elif event.key == pygame.K_LEFT:
                player.dx = -10
            elif event.key == pygame.K_RIGHT:
                player.dx = 10
            elif event.key == pygame.K_UP:
                player.dy = -10
            elif event.key == pygame.K_DOWN:
                player.dy = 10
        elif event.type == pygame.KEYUP:
            if keystate[K_LEFT] == 0 and keystate[K_RIGHT] == 0 and \
                            keystate[K_UP] == 0 and keystate[K_DOWN] == 0:
                player.dx = 0
                player.dy = 0
            else:
                pass
