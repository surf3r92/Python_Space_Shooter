import os, sys, pygame, random
from pygame.locals import *
from lib.buttons import *
from lib.input import *
from highscore import *


class Menu:
    def __init__(self):
        pass


def gameMenu(self):
    if self.gameState == "Start":
        menuBackground = pygame.image.load("img/sprites/startscreen.png")
        self.screen.blit(menuBackground, (0, 0))
    elif self.gameState == "Gameover":
        menuBackground = pygame.image.load("img/sprites/gameover_screen.png")
        self.screen.blit(menuBackground, (0, 0))


    # self.playerlives.append(
    #     (self.playerLivesPictures, 32 + (32 + self.playerLivesPictures.get_width()) * 0, self.height -
    #      self.playerLivesPictures.get_height() - 16))
    # self.playerlives.append((self.playerLivesPictures, 32 + (self.playerLivesPictures.get_width()) * 1, self.height -
    #                          self.playerLivesPictures.get_height() - 16))
    # self.playerlives.append((self.playerLivesPictures, 32 + (self.playerLivesPictures.get_width()) * 2, self.height -
    #                          self.playerLivesPictures.get_height() - 16))

    buttonWidth = 0
    buttonHeight = 50
    buttonLength = 200
    buttonYDist = 100
    buttonXPos = (self.screen.get_size()[0] / 2) - (buttonLength / 2)
    buttonColor = (46, 46, 254)
    buttonColorHovered = (8, 8, 138)
    buttonTextColor = (255, 255, 255)
    buttonTextFont = self.fontLink
    buttonTextFontSize = 20

    button1YPos = (self.screen.get_size()[1] / 2) - (buttonHeight / 2) - buttonYDist
    button2YPos = (self.screen.get_size()[1] / 2) - (buttonHeight / 2)
    button3YPos = (self.screen.get_size()[1] / 2) + (buttonHeight / 2) + (buttonYDist - buttonHeight)

    if self.gameState == "Start":
        button1Text = "Start Game"
        button2Text = "Highscore"
        button3Text = "Quit"
    elif self.gameState == "Pause":
        button1Text = "Continue"
        button2Text = "Restart"
        button3Text = "Menu"
    elif self.gameState == "Gameover":
        button1Text = "Restart"
        button2Text = "Highscore"
        button3Text = "Menu"

    inputMaxLength = 12
    inputTextColor = (255, 255, 255)

    inputText = ""
    if self.gameState == "Start":
        inputText = 'Enter your name!'
    else:
        inputText = self.currUserName

    inputTextFont = self.fontLink
    inputTextFontSize = 18
    inputRectColor = (0, 0, 255)
    inputRectLength = 200
    inputRectHeight = inputTextFontSize*1.8
    inputYPos = button3YPos + 3 * buttonHeight
    inputXPos = (self.screen.get_size()[0] / 2) - (inputRectLength / 2)

    inputBox = Input(self.screen, inputXPos, inputYPos, inputMaxLength, inputTextColor, inputText, inputRectColor,
                     inputRectLength, inputRectHeight, inputTextFont, inputTextFontSize)

    button1 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button1YPos, buttonLength, buttonHeight,
                     buttonWidth, button1Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
    button2 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button2YPos, buttonLength, buttonHeight,
                     buttonWidth, button2Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
    button3 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button3YPos, buttonLength, buttonHeight,
                     buttonWidth, button3Text, buttonTextColor, buttonTextFont, buttonTextFontSize)

    allButtons = [button1, button2, button3]

    keepGoing = True
    onStartClicked = False;

    while keepGoing:
        pygame.mouse.set_visible(1)

        # hintergrundfarbe
        # screen.fill((30,144,255))

        button1.create_button()
        button2.create_button()
        button3.create_button()

        global currUserName

        pygame.display.flip()
        for event in pygame.event.get():

            if self.gameState == "Start":
                inputBox.update(event)
                inputBox.draw(self.screen)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button1.pressed(pygame.mouse.get_pos()):
                    if self.gameState == "Start" or self.gameState == "Pause" or self.gameState == "Gameover":
                        #print "input: " + inputBox.getText()
                        #print "name: " + self.currUserName

                        if inputBox.getText() == 'Enter your name!':
                            self.currUserName = "unknown"
                        else:
                            self.currUserName = inputBox.getText()

                        if self.gameState == "Start":
                            # self.game()
                            self.setupNewGame()
                        elif self.gameState == "Pause":
                            self.gameState = "Start"
                            keepGoing = False
                        elif self.gameState == "Gameover":
                            self.gameState = "Start"
                            keepGoing = False
                            self.setupNewGame()
                    else:
                        pass
                if button2.pressed(pygame.mouse.get_pos()):
                    if self.gameState == "Start" or self.gameState == "Gameover":
                        self.callHighscore()
                    elif self.gameState == "Pause":
                        self.gameState = "Start"
                        keepGoing = False
                        self.setupNewGame()
                if button3.pressed(pygame.mouse.get_pos()):
                    if self.gameState == "Start":
                        pygame.quit()
                        sys.exit()
                    elif self.gameState == "Pause" or self.gameState == "Gameover":
                        self.gameState = "Start"
                        gameMenu(self)
            elif event.type == MOUSEMOTION:
                for currButton in allButtons:
                    if currButton.getRect().collidepoint(pygame.mouse.get_pos()):
                        currButton.setHovered()
                    else:
                        currButton.setUnhovered()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = "Start"
                    keepGoing = False
                ENTER_KEY_CODE = 13
                if event.key == ENTER_KEY_CODE:
                    if self.gameState == "Start":
                        self.setupNewGame()
