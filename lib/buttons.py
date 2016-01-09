import pygame
from pygame.locals import *
pygame.init()
class Button:
    def __init__(self, surface, color, color_hovered, x, y, length, height, width, text, text_color, text_font, font_size):
        self.hoverState = False

        self.surface = surface
        self.color = color
        self.color_hovered = color_hovered
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.text_font = text_font
        self.font_size = font_size

    def create_button(self):
        # surface = ...  sowie return statement kann weggelassen werden
        if self.hoverState:
            surface = self.draw_button(self.color_hovered)
        else:
            surface = self.draw_button(self.color)
        surface = self.write_text()
        self.rect = pygame.Rect(self.x,self.y, self.length, self.height)
        return surface

    def write_text(self):
        myFont = pygame.font.SysFont(self.text_font, self.font_size)
        myText = myFont.render(self.text, 1, self.text_color)
        self.surface.blit(myText, ((self.x+self.length/2) - myText.get_width()/2, (self.y+self.height/2) - myText.get_height()/2))
        return self.surface

    def draw_button(self, color):
        #erzeugt den Rahmen der Buttons
        for i in range(1,2):
            s = pygame.Surface((self.length+(10*2),self.height+(10*2)))
            s.fill(color)
            s.set_alpha(5)
            pygame.draw.rect(s, color, (self.x-10,self.y-10,self.length+10,self.height+10), self.width)
            self.surface.blit(s, (self.x-10,self.y-10))
        pygame.draw.rect(self.surface, color, (self.x,self.y,self.length,self.height), 0)
        pygame.draw.rect(self.surface, (190,190,190), (self.x,self.y,self.length,self.height), 1)
        return self.surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

    def getRect(self):
        return self.rect

    def getText(self):
        return self.text

    def setHovered(self):
        self.hoverState = True

    def setUnhovered(self):
        self.hoverState = False

    def setText(self, newText):
        self.text = newText

    def getText(self):
        return self.text