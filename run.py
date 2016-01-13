import os, sys, pygame, random
from pygame.locals import *
from lib.arena import *
from lib.player import *
from lib.buttons import *
from lib.input import *
from lib.enemy import *
from lib.highscore import *
from lib.menu import *

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
        print self
        gameMenu(self)

    # enemies = []
    
    def callHighscore(self):
        highScore(self)

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
                
                # Update
                #screen.blit(background, (0, 0))
                playerSprite.update()
                arena.update(self.screen)
                laserSprites.update()
                enemies.update()
                enemyLaserSprites.update()
    
                scoreDisplay = self.myFont.render("".join(["Score:",str(self.score)]), 1, self.green)
                self.screen.blit(scoreDisplay, (self.width-160, self.height-self.playerLivesPictures.get_height()-24))
    
                for lives in self.playerlives:
                    self.screen.blit(lives[0], (lives[1], lives[2]))
    
                collide_list = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
                if(collide_list != {}):
                    self.score += 10
                    print self.score
                player_hit = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
                # spritecollide kann noch erweitert werden mit callback function wenn player getroffen wird
                # spritecollide(sprite, group, dokill, collided = None)
                if len(player_hit) > 0:
                    print "player hit"
                    if len(self.playerlives) > 0:
                        self.playerlives.pop(-1)
                    print self.playerlives
                    if len(self.playerlives) == 0:
                        print "game over"
                        self.gameState = "Gameover"
                        gameMenu(self)
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



run()
