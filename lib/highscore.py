import os, sys, pygame, random
from pygame.locals import *

class HighScore:
    def __init__(self, screen, list, x, y, color, length, height, text_font, font_size, text_color):
        self.list = list
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.height = height
        self.text_font = text_font
        self.font_size = font_size
        self.text_color = text_color

    def create_list(self):
        self.draw()
        for index in range(0,len(self.list)):
            self.write_text(self.list[index][0], self.list[index][1], index)
        self.rect = pygame.Rect(self.x,self.y, self.length, self.height)

    def write_text(self, key, value, index):
        myFont = pygame.font.SysFont(self.text_font, self.font_size)

        key = myFont.render(key, 1, self.text_color)
        colon = myFont.render(":", 1, self.text_color)
        value = myFont.render(value, 1, self.text_color)
        listingNum = myFont.render(str(index+1) + ".", 1, self.text_color)

        mediumDist = 20
        yPos = (self.y + index*30 + 20)

        self.screen.blit(key, ((self.x+self.length/2) - key.get_width() - mediumDist, yPos))
        self.screen.blit(colon, ((self.x+self.length/2) - colon.get_width()/2, yPos))
        self.screen.blit(value, ((self.x+self.length/2) + mediumDist, yPos))
        self.screen.blit(listingNum, (self.x - listingNum.get_width() + 70, yPos))
        return self.screen

    def draw(self):
        #pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.length,self.height), 0)
        return self.screen