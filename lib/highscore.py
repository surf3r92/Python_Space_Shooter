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
        for element in self.list:
            self.write_text(element, self.list[element])
        self.rect = pygame.Rect(self.x,self.y, self.length, self.height)

    def write_text(self, key, value):
        myFont = pygame.font.SysFont(self.text_font, self.font_size)
        myText = myFont.render(key + ": " + value, 1, self.text_color)
        self.screen.blit(myText, ((self.x+self.length/2) - myText.get_width()/2, (self.y+self.height/2) - myText.get_height()/2))
        return self.screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.length,self.height), 0)
        return self.screen