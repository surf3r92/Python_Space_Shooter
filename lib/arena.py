import os, sys, pygame, random
from pygame.locals import *
from lib.methods import *

class Arena ():

    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)

        self.background1 = pygame.image.load("img/sprites/background.png")
        self.background2 = pygame.image.load("img/sprites/background.png")


        self.background1_y = -600
        self.background2_y = -1800


    def update(self, screen):

        screen.blit(self.background1, (0, self.background1_y))
        screen.blit(self.background2, (0, self.background2_y))


        self.background1_y += 3
        self.background2_y += 3

        if self.background1_y >= 600:
            print("background1")
            self.reset()
        if self.background2_y >= 600:
            print("background2")
            self.reset2()



    def reset(self):
            self.background1_y = self.background2_y - self.background2.get_height() #-1800

    def reset2(self):
        self.background2_y = self.background1_y - self.background1.get_height() #-1800

