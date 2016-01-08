import os, sys, pygame, random
from pygame.locals import *
from lib.arena import *
from lib.player import *
from lib.buttons import *
from lib.input import *
from lib.enemy import *

os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("img/sprites/Space Shooter.png")
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

gameState = "Start"
currUserName = ""

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# enemies = []


def game():

    # Game Objects
    global player
    player = Player()

    playerSprite = pygame.sprite.RenderPlain((player))

    # global enemy
    # enemy = Enemy()
	
    # Arena
    arena = Arena()
    #arena = pygame.sprite.RenderPlain((arena))

    # Projectiles
	
	

    clock = pygame.time.Clock()
    keepgoing = True
    frameCounter = 0
    pygame.key.set_repeat(10, 10)
    while keepgoing:
		
        global gameState
        if gameState == "Start":
            pygame.mouse.set_visible(0)
            clock.tick(30)
            frameCounter += 1
			
            if frameCounter%30 == 0:
                # newEnemy = Enemy(random.randint(1,4)*100, -50)
                # enemies.append(newEnemy)
                enemies.add(Enemy((random.randint(1,7)*100,50)))
                # print "new Enemy created"


            for event in pygame.event.get():
                keystate = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    keepgoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #keepgoing = False
                        gameState = "Pause"
                        gameMenu()
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
            arena.update(screen)
            laserSprites.update()
            enemies.update()
            enemyLaserSprites.update()

            collide_list = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
            player_hit = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
            # spritecollide kann noch erweitert werden mit callback function wenn player getroffen wird
            # spritecollide(sprite, group, dokill, collided = None)
            if len(player_hit) > 0:
                print "player hit"
            # Draw
            #arena.draw(screen)
            playerSprite.draw(screen)
            laserSprites.draw(screen)
            enemies.draw(screen)
            enemyLaserSprites.draw(screen)
			
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

def gameMenu():

    if gameState == "Start":
        menuBackground = pygame.image.load("img/sprites/startscreen.png")
        screen.blit(menuBackground, (0, 0))


    buttonWidth = 0
    buttonHeight = 50
    buttonLength = 200
    buttonYDist = 100
    buttonXPos = (screen.get_size()[0]/2) - (buttonLength/2)
    buttonColor = (46,46,254)
    buttonColorHovered = (8,8,138)
    buttonTextColor = (255,255,255)
    buttonTextFont = "Calibri"
    buttonTextFontSize = 20

    button1YPos = (screen.get_size()[1]/2) - (buttonHeight/2) - buttonYDist
    button2YPos = (screen.get_size()[1]/2) - (buttonHeight/2)
    button3YPos = (screen.get_size()[1]/2) + (buttonHeight/2) + (buttonYDist - buttonHeight)

    global gameState
    if gameState == "Start":
        button1Text = "Start Game"
    else:
        button1Text = "Continue"
    button2Text = "High Score"
    button3Text = "Quit"

    inputMaxLength = 20
    inputTextColor = (255,255,255)
    inputText = 'Enter your name!'
    inputTextFont = "Calibri"
    inputTextFontSize = 20
    inputRectColor = (0,0,255)
    inputRectLength = 200
    inputRectHeight = inputTextFontSize
    inputYPos = button3YPos + 3* buttonHeight
    inputXPos = (screen.get_size()[0]/2) - (inputRectLength/2)

    #if gameState == "Start":
    #    inputText = 'Enter your name!'

    inputBox = Input(screen, inputXPos, inputYPos, inputMaxLength, inputTextColor, inputText, inputRectColor, inputRectLength, inputRectHeight, inputTextFont, inputTextFontSize)

    button1 = Button(screen, buttonColor, buttonColorHovered, buttonXPos, button1YPos, buttonLength, buttonHeight, buttonWidth, button1Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
    button2 = Button(screen, buttonColor, buttonColorHovered, buttonXPos, button2YPos, buttonLength, buttonHeight, buttonWidth, button2Text, buttonTextColor, buttonTextFont, buttonTextFontSize)
    button3 = Button(screen, buttonColor, buttonColorHovered, buttonXPos, button3YPos, buttonLength, buttonHeight, buttonWidth, button3Text, buttonTextColor, buttonTextFont, buttonTextFontSize)

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

            if onStartClicked and gameState == "Start":
                inputBox.update(event)
                inputBox.draw(screen)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button1.pressed(pygame.mouse.get_pos()):

                    if inputBox.getText() != inputText or gameState == "Pause":
                        print button1Text
                        currUserName = inputBox.getText()
                        if button1.getText() == "Start Game":
                            button1.setText("Continue")
                            game()
                        else:
                            gameState = "Start"
                            keepGoing = False
                    else:
                        onStartClicked = True
                if button2.pressed(pygame.mouse.get_pos()):
                    print button2Text
                if button3.pressed(pygame.mouse.get_pos()):
                    print button3Text
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEMOTION:
                for currButton in allButtons:
                    if currButton.getRect().collidepoint(pygame.mouse.get_pos()):
                        currButton.setHovered()
                    else:
                        currButton.setUnhovered()

gameMenu()