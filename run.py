import os, sys, pygame, random
from pygame.locals import *
from lib.highscore import *
from lib.arena import arena
from lib.player import *
from lib.enemy import *
from lib.menu import *


class Run():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = "1"
        pygame.init()
        pygame.display.set_caption("Space Shooter")

        self.icon = pygame.image.load("img/sprites/Space Shooter.png")
        self.playerLivesPictures = pygame.image.load("img/sprites/player.png")
        self.green = 0, 255, 0
        self.score = 0

        # self.playerlives = []

        self.lives = 3

        self.myFont = pygame.font.SysFont("monospace", 24)
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)

        self.gameState = "Start"
        self.currUserName = ""

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        gameMenu(self)


    def callHighscore(self):
        highScore(self)

    def callGame(self):
        self.game()

    def game(self):
        # Game Objects
        global player
        player = Player()

        playerSprite = pygame.sprite.RenderPlain((player))

        global enemy
        global enemyLaserSprites
        global laserSprites

        self.livesImage, self.livesRect = load_image("img/sprites/ship.png", -1)
        self.livesImage = pygame.transform.scale(self.livesImage, (int(self.livesImage.get_width()*0.75), int(self.livesImage.get_height()*0.75)))
        # lives vllt noch auslagern, in update einbeziehen, zZ noch unter arena

        # score
        # score ausgelagert in score.py aber noch fehlerhaft, noch in update einbeziehen, zZ noch unter arena

        clock = pygame.time.Clock()
        keepgoing = True
        frameCounter = 0
        pygame.key.set_repeat(10, 10)
        while keepgoing:

            clock.tick(30)
            caption = "Space Shooter - FPS: {0:.2f}".format(clock.get_fps())
            pygame.display.set_caption(caption)

            if self.gameState == "Start" or self.gameState == "Gameover":
                # or gameState == "Restart"\
                # if gameState == "Restart":
                # gameState = "Start"
                # keepgoing = False
                if self.gameState == "Gameover":
                    keepgoing = False
                pygame.mouse.set_visible(0)

                frameCounter += 1

                if frameCounter % 60 == 1:
                    enemies.add(Enemy((-50 + random.randint(1, 7) * 100, random.randint(-50, 0))))

                keyControls(self, player)

                # Update
                playerSprite.update()
                arena.update(self.screen)
                laserSprites.update()
                enemies.update()
                enemyLaserSprites.update()

                scoreDisplay = self.myFont.render("".join(["Score:", str(self.score)]), 1, self.green)
                self.screen.blit(scoreDisplay,(self.width - 160, self.height - 48))
                #
                # for lives in self.playerlives:
                #     self.screen.blit(lives[0], (lives[1], lives[2]))

                collide_list = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
                if (collide_list != {}):
                    self.score += 10
                    print self.score
                player_hit = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
                if len(player_hit):
                    self.lives -= 1
                    print "player hit"
                if self.lives == 0:
                    print "game over"
                    self.gameState = "Gameover"
                    gameMenu(self)
                # spritecollide kann noch erweitert werden mit callback function wenn player getroffen wird
                # spritecollide(sprite, group, dokill, collided = None)

                pygame.draw.line(self.screen, (0,194,244), (0, self.height - 60), (self.width,self.height - 60), 4)
                playerSprite.draw(self.screen)
                laserSprites.draw(self.screen)
                enemies.draw(self.screen)
                enemyLaserSprites.draw(self.screen)

                for i in range(0,self.lives):
                    self.screen.blit(self.livesImage,(8 + i*self.livesImage.get_width()*1.5,self.height  - self.livesImage.get_height()-8))

                pygame.display.flip()


    def setupNewGame(self):
        enemies.empty()
        enemyLaserSprites.empty()
        laserSprites.empty()
        self.lives = 3
        self.score = 0
        self.game()

Run()
