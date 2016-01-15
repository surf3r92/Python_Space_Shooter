import os, sys, pygame, random
from pygame.locals import *
from lib.buttons import *
from lib.menu import *


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
        for index in range(0, len(self.list)):
            self.write_text(self.list[index][0], self.list[index][1], index)
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def write_text(self, key, value, index):
        myFont = pygame.font.SysFont(self.text_font, self.font_size)

        key = myFont.render(key, 1, self.text_color)
        colon = myFont.render(":", 1, self.text_color)
        value = myFont.render(value, 1, self.text_color)
        listingNum = myFont.render(str(index + 1) + ".", 1, self.text_color)

        mediumDist = 20
        yPos = (self.y + index * 30 + 20)

        self.screen.blit(key, ((self.x + self.length / 2) - key.get_width() - mediumDist, yPos))
        self.screen.blit(colon, ((self.x + self.length / 2) - colon.get_width() / 2, yPos))
        self.screen.blit(value, ((self.x + self.length / 2) + mediumDist, yPos))
        self.screen.blit(listingNum, (self.x - listingNum.get_width() + 70, yPos))
        return self.screen

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.length,self.height), 0)
        return self.screen




def highScore(self):

    if self.gameState == "Start" or self.gameState == "Gameover":
        highscoreBackground = pygame.image.load("img/sprites/highscore_screen.png")
        self.screen.blit(highscoreBackground, (0, 0))

    list = []
    highscoreList = self.highscoreList
    for highscoreElement in highscoreList:
        highscoreElementListWithoutEnd = highscoreElement.strip()
        highscoreElementList = highscoreElementListWithoutEnd.split(",")
        print highscoreElementList
        list.append((highscoreElementList[0],highscoreElementList[1]))

        try:
            list.append((highscoreElementList[0],highscoreElementList[1]))
        except:
            print "Highscore Element has no Score or Name Value"
    heighScoreHeight = 350
    heighScoreLength = 330
    heighScoreXPos = (self.screen.get_size()[0] / 2) - (heighScoreLength / 2)
    heighScoreYPos = (self.screen.get_size()[1] / 2) - (heighScoreHeight / 2) + 25
    heighScoreColor = (46, 46, 254)
    heighScoreTextFont = "Calibri"
    heighScoreTextFontSize = 20
    heighScoreTextColor = (255, 255, 255)

    highScoreList = HighScore(self.screen, list, heighScoreXPos, heighScoreYPos, heighScoreColor, heighScoreLength,
                              heighScoreHeight, heighScoreTextFont, heighScoreTextFontSize, heighScoreTextColor)

    buttonWidth = 0
    buttonHeight = 50
    buttonLength = 200
    buttonYDist = 50
    buttonXDist = buttonYDist
    buttonXPos = (self.screen.get_size()[0]) - (buttonLength) - buttonXDist
    buttonColor = (46, 46, 254)
    buttonColorHovered = (8, 8, 138)
    buttonTextColor = (255, 255, 255)
    buttonTextFont = "Calibri"
    buttonTextFontSize = 20

    buttonBackYPos = (self.screen.get_size()[1]) - (buttonHeight) - buttonYDist
    buttonBackText = "Back"

    buttonBack = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, buttonBackYPos, buttonLength,
                        buttonHeight, buttonWidth, buttonBackText, buttonTextColor, buttonTextFont, buttonTextFontSize)

    keepGoing = True
    allButtons = [buttonBack]

    while keepGoing:
        pygame.mouse.set_visible(1)
        highScoreList.create_list()
        buttonBack.create_button()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if buttonBack.pressed(pygame.mouse.get_pos()):
                    keepGoing = False
                    gameMenu(self)
            elif event.type == MOUSEMOTION:
                for currButton in allButtons:
                    if currButton.getRect().collidepoint(pygame.mouse.get_pos()):
                        currButton.setHovered()
                    else:
                        currButton.setUnhovered()

def updateHighscore(self, playerName, playerScore):
    bool = False
    for index in range(0,len(self.highscoreList)):
        if int(self.highscoreList[index].split(",")[1]) < playerScore:
            self.highscoreList.insert(index,playerName + "," + str(playerScore))
            bool = True
            break
    if bool == False and len(self.highscoreList) < 10:
        self.highscoreList.append(playerName + "," + str(playerScore))

    file = open("csv/highscore.csv", "w")
    file.truncate()
    for element in self.highscoreList:
        string = element + "\n"
        file.write(string)
    file.close()
