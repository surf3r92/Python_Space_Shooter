import os, sys, pygame, random
from pygame.locals import *
from lib.arena import *
from lib.player import *
from lib.buttons import *
from lib.input import *
from lib.enemy import *
from lib.highscore import *

class run():

    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = "1"
        pygame.init()
        pygame.display.set_caption("Space Shooter")
        self.icon = pygame.image.load("img/sprites/Space Shooter.png")
        self.playerLivesPictures = pygame.image.load("img/sprites/player.png")
        self.green = 0,255,0
        self.score = 0
        self.playerlives = []
        self.myFont = pygame.font.SysFont("monospace",24)
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)

        self.gameState = "Start"
        self.currUserName = ""

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        self.gameMenu()

    # enemies = []
    
    
    def game(self):
    
        # Game Objects
        global player
        player = Player()
    
        playerSprite = pygame.sprite.RenderPlain((player))
    
        # global enemy
        # enemy = Enemy()
        
        # Arena
        arena = Arena()
        #arena = pygame.sprite.RenderPlain((arena))
    
        #lives vllt noch auslagern, in update einbeziehen, zZ noch unter arena
    
        #score
        global score
        #score ausgelagert in score.py aber noch fehlerhaft, noch in update einbeziehen, zZ noch unter arena
    
    
    
        # Projectiles
        
        
    
        clock = pygame.time.Clock()
        keepgoing = True
        frameCounter = 0
        pygame.key.set_repeat(10, 10)
        while keepgoing:
            
            if self.gameState == "Start" or self.gameState == "Gameover":
                    #or gameState == "Restart"\
                #if gameState == "Restart":
                    #gameState = "Start"
                    #keepgoing = False
                if self.gameState == "Gameover":
                    keepgoing = False
                pygame.mouse.set_visible(0)
                clock.tick(30)
                frameCounter += 1
                
                if frameCounter%60 == 1:
                    # newEnemy = Enemy(random.randint(1,4)*100, -50)
                    # enemies.append(newEnemy)
                    enemies.add(Enemy((-50 + random.randint(1,7)*100,random.randint(-50,0))))
                    # print "new Enemy created"
    
    
                for event in pygame.event.get():
                    keystate = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        keepgoing = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            #keepgoing = False
                            self.gameState = "Pause"
                            self.gameMenu()
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
                
                # Update
                #screen.blit(background, (0, 0))
                playerSprite.update()
                arena.update(self.screen)
                laserSprites.update()
                enemies.update()
                enemyLaserSprites.update()
    
                scoreDisplay = self.myFont.render("".join(["Score:",str(score)]), 1, self.green)
                self.screen.blit(scoreDisplay, (self.width-160, self.height-self.playerLivesPictures.get_height()-24))
    
                for lives in playerlives:
                    self.screen.blit(lives[0], (lives[1], lives[2]))
    
                collide_list = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
                if(collide_list != {}):
                    score += 10
                    print score
                player_hit = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
                # spritecollide kann noch erweitert werden mit callback function wenn player getroffen wird
                # spritecollide(sprite, group, dokill, collided = None)
                if len(player_hit) > 0:
                    print "player hit"
                    if len(playerlives) > 0:
                        playerlives.pop(-1)
                    print playerlives
                    if len(playerlives) == 0:
                        print "game over"
                        self.gameState = "Gameover"
                        self.gameMenu()
                        #endgame
                # Draw
                #arena.draw(screen)
                playerSprite.draw(self.screen)
                laserSprites.draw(self.screen)
                enemies.draw(self.screen)
                enemyLaserSprites.draw(self.screen)
                
                # for enemy in enemies: 
                    # enemy.update(random.randint(0,7),random.randint(0,5))
                    
                    # screen.blit(enemy.image, (enemy.x, enemy.y))
                    
                # for eLaser in enemyLaserSprites: 
                    # eLaser.update()
                    # screen.blit(eLaser.image, (eLaser.x, eLaser.y))
                    # if eLaser.x > 600:
                        # enemyLaserSprites.remove(eLaser)
                
                # print laserSprites
                
                # print laserSprites
                            
                pygame.display.flip()
    
    
    
    

    
    
    
    def gameMenu(self):
    
        if self.gameState == "Start":
            menuBackground = pygame.image.load("img/sprites/startscreen.png")
            self.screen.blit(menuBackground, (0, 0))
    
        global score
        global playerlives
    
        score = 0
    
        playerlives = []
        playerlives.append((self.playerLivesPictures, 32 + (32+self.playerLivesPictures.get_width())*0, self.height - self.playerLivesPictures.get_height()-16))
        playerlives.append((self.playerLivesPictures, 32 + (32+self.playerLivesPictures.get_width())*1, self.height - self.playerLivesPictures.get_height()-16))
        playerlives.append((self.playerLivesPictures, 32 + (32+self.playerLivesPictures.get_width())*2, self.height - self.playerLivesPictures.get_height()-16))
    
        buttonWidth = 0
        buttonHeight = 50
        buttonLength = 200
        buttonYDist = 100
        buttonXPos = (self.screen.get_size()[0]/2) - (buttonLength/2)
        buttonColor = (46,46,254)
        buttonColorHovered = (8,8,138)
        buttonTextColor = (255,255,255)
        buttonTextFont = "Calibri"
        buttonTextFontSize = 20
    
        button1YPos = (self.screen.get_size()[1]/2) - (buttonHeight/2) - buttonYDist
        button2YPos = (self.screen.get_size()[1]/2) - (buttonHeight/2)
        button3YPos = (self.screen.get_size()[1]/2) + (buttonHeight/2) + (buttonYDist - buttonHeight)
    
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
    
        inputMaxLength = 20
        inputTextColor = (255,255,255)
        inputText = 'Enter your name!'
        inputTextFont = "Calibri"
        inputTextFontSize = 20
        inputRectColor = (0,0,255)
        inputRectLength = 200
        inputRectHeight = inputTextFontSize
        inputYPos = button3YPos + 3* buttonHeight
        inputXPos = (self.screen.get_size()[0]/2) - (inputRectLength/2)
    
        inputBox = Input(self.screen, inputXPos, inputYPos, inputMaxLength, inputTextColor, inputText, inputRectColor, inputRectLength, inputRectHeight, inputTextFont, inputTextFontSize)
    
        button1 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button1YPos, buttonLength, buttonHeight, buttonWidth, button1Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
        button2 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button2YPos, buttonLength, buttonHeight, buttonWidth, button2Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
        button3 = Button(self.screen, buttonColor, buttonColorHovered, buttonXPos, button3YPos, buttonLength, buttonHeight, buttonWidth, button3Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
    
        allButtons = [button1, button2, button3]
    
        keepGoing = True
        onStartClicked = False;
    
        while keepGoing:
            pygame.mouse.set_visible(1)
    
            #hintergrundfarbe
            #screen.fill((30,144,255))
    
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
                        if inputBox.getText() != inputText or self.gameState == "Pause":
                            print button1Text
                            currUserName = inputBox.getText()
                            if self.gameState == "Start":
                                self.game()
                            elif self.gameState == "Pause":
                                self.gameState = "Start"
                                keepGoing = False
                            elif self.gameState == "Gameover":
                                pass
                        else:
                            inputBox.setTextColor((255,0,0))
                    if button2.pressed(pygame.mouse.get_pos()):
                        print button2Text
                        if self.gameState == "Start" or self.gameState == "Gameover":
                            highScore(self)
                        elif self.gameState == "Pause":
                            #hier Restart einleisten ohne gameState = "Start"
                            self.gameState = "Start"
                            keepGoing = False
                    if button3.pressed(pygame.mouse.get_pos()):
                        print button3Text
                        if self.gameState == "Start":
                            pygame.quit()
                            sys.exit()
                        elif self.gameState == "Pause" or self.gameState == "Gameover":
                            self.gameState = "Start"
                            self.gameMenu()
                elif event.type == MOUSEMOTION:
                    for currButton in allButtons:
                        if currButton.getRect().collidepoint(pygame.mouse.get_pos()):
                            currButton.setHovered()
                        else:
                            currButton.setUnhovered()
run()