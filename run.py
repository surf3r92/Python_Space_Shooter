import os, sys, pygame, random
from pygame.locals import *
from lib.highscore import *
from lib.arena import arena
from lib.player import *
from lib.enemy import *
from lib.powerup import *
from lib.menu import *
from lib.boss import *


class Run():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = "1"
        pygame.init()
        pygame.display.set_caption("Space Shooter")

        self.icon = pygame.image.load("img/sprites/Space Shooter.png")
        self.playerLivesPictures = pygame.image.load("img/sprites/player.png")
        self.blue = 0,194,244
        self.score = 0
        self.highscoreList = open("csv/highscore.csv").read().split()
        self.lives = 3

        self.enemiesSpawned = 0
        self.level = 0

        self.myFont = pygame.font.SysFont("monospace", 24)
        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)

        self.gameState = "Start"
        self.userNameUnknown = "unknown"
        self.currUserName = ""

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        self.xGroup = 0
        self.xPowerups = 0

        self.randomPowerup = ""
        self.laserMax = 20
        self.damage = 1
        self.shield = False

        global player
        player = Player()

        global playerSprite
        playerSprite = pygame.sprite.RenderPlain((player))

        gameMenu(self)

    def callHighscore(self):
        highScore(self)

    def callGame(self):
        self.game()

    def game(self):

        global enemy
        global enemyLaserSprites
        global laserSprites
        global laserPowerup

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
                if self.gameState == "Gameover":
                    keepgoing = False
                pygame.mouse.set_visible(0)

                frameCounter += 1

                if frameCounter % 100 == 1 and frameCounter > 200:
                    self.xPowerups = random.randint(1, 7) * 100 - 50
                    randomInt = random.randint(0, 3)
                    if randomInt == 0:
                        self.randomPowerup = "fasterLaser"
                    elif randomInt == 1:
                        self.randomPowerup = "health"
                    elif randomInt == 2:
                        self.randomPowerup = "shield"
                    elif randomInt == 3:
                        self.randomPowerup = "multipleShoot"
                    laserPowerups.add(Powerup((self.xPowerups, -20), self.randomPowerup))

                if len(boss.sprites()) == 1:
                    if boss.sprites()[0].health == 0:
                        boss.sprites()[0].kill()
                        self.score += 1000
                        self.nextLevel()

                if self.enemiesSpawned < 20:
                    if frameCounter % 200 == 1 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 200 == 21 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 200 == 41 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 200 == 61 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 400 == 81 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 400 == 101 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 400 == 121 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))

                    if frameCounter % 400 == 141 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        enemies.add(Enemy((self.xGroup, -20)))
                elif len(enemies.sprites()) == 0 and len(boss.sprites()) == 0:
                    boss.add(Boss((self.width/2, -50)))

                keyControls(self, player)

                # Update
                playerSprite.update(self.damage)
                arena.update(self.screen)
                laserSprites.update()
                bossLaserSprites.update()
                enemies.update()
                enemyLaserSprites.update()
                boss.update()
                laserPowerups.update()

                if frameCounter < 80 and self.level == 1:
                    readyText = self.myFont.render("".join(["GET READY!", str("")]), 1, (200, 10, 10))
                    self.screen.blit(readyText, (self.width/2 - 64, self.height/3))
                elif frameCounter < 140 and self.level == 1:
                    levelText = self.myFont.render("".join(["LEVEL ", str(self.level)]), 1, (200, 10, 10))
                    self.screen.blit(levelText, (self.width/2 - 64, self.height/3))
                elif frameCounter < 170 and self.level == 1:
                    goText = self.myFont.render("".join(["GO!", str("")]), 1, (200, 10, 10))
                    self.screen.blit(goText, (self.width/2 - 20, self.height/3))

                if self.level > 1:
                    if frameCounter < 80:
                        readyText = self.myFont.render("".join(["LEVEL COMPLETED!!", str("")]), 1, (200, 10, 10))
                        self.screen.blit(readyText, (self.width/2 - 100, self.height/3))
                    elif frameCounter < 140:
                        levelText = self.myFont.render("".join(["LEVEL ", str(self.level)]), 1, (200, 10, 10))
                        self.screen.blit(levelText, (self.width/2 - 64, self.height/3))
                    elif frameCounter < 170:
                        goText = self.myFont.render("".join(["GO!", str("")]), 1, (200, 10, 10))
                        self.screen.blit(goText, (self.width/2 - 20, self.height/3))

                pygame.draw.rect(self.screen,(0,0,0),(0,self.height-60,self.width,self.height))
                pygame.draw.line(self.screen, (0,194,244), (0, self.height - 60), (self.width,self.height - 60), 4)

                scoreDisplay = self.myFont.render("".join(["Score:", str(self.score)]), 1, self.blue)
                self.screen.blit(scoreDisplay, (self.width - 160, self.height - 48))

                boss_hit = pygame.sprite.groupcollide(laserSprites, boss, True, False)
                if boss_hit != {}:
                    boss.sprites()[0].health -= 1

                collide_list = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
                if (collide_list != {}):
                    self.score += 10
                player_hit = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
                if len(player_hit):
                    self.lives -= 1
                if self.lives == 0:
                    self.gameState = "Gameover"
                    updateHighscore(self, self.currUserName, self.score)
                    gameMenu(self)
                powerup_collected = pygame.sprite.spritecollide(player, laserPowerups, True)
                if len(powerup_collected):
                    if self.randomPowerup == "fasterLaser":
                       player.decreaseLaser()
                    elif self.randomPowerup == "health":
                        self.lives += 1
                    elif self.randomPowerup == "multipleShoot":
                        self.damage += 1
                    elif self.randomPowerup == "shield":
                        self.shield = True
                        shieldTime = frameCounter
                        playerPos = playerSprite.sprites()[0].rect.center
                        playerSprite.sprites()[0].image, playerSprite.sprites()[0].rect = \
                            load_image("img/sprites/shipWithShield.png", -1)
                        playerSprite.sprites()[0].rect.center = playerPos
                collide_Player_Enemy = pygame.sprite.spritecollide(player, enemies, True)

                if len(collide_Player_Enemy):
                    self.lives -= 1

                if self.shield == True:
                    if (frameCounter - shieldTime) > 100:
                        self.shield = False
                        playerPos = playerSprite.sprites()[0].rect.center
                        playerSprite.sprites()[0].image, playerSprite.sprites()[0].rect = \
                            load_image("img/sprites/ship.png", -1)
                        playerSprite.sprites()[0].rect.center = playerPos

                playerSprite.draw(self.screen)
                laserSprites.draw(self.screen)
                bossLaserSprites.draw(self.screen)
                enemies.draw(self.screen)
                enemyLaserSprites.draw(self.screen)
                boss.draw(self.screen)
                laserPowerups.draw(self.screen)

                for i in range(0, self. lives):
                    self.screen.blit(self.livesImage, (8 + i*self.livesImage.get_width()*1.5, self.height -
                                                       self.livesImage.get_height()-8))
                pygame.display.flip()

    def nextLevel(self):
        self.resetSprites()
        self.level += 1
        self.game()

    def setupNewGame(self):
        player.rect.center = (400, 500)
        self.resetPowerups()
        self.resetSprites()
        self.lives = 3
        self.score = 0
        self.level = 1
        laserPowerups.empty()
        self.game()

    def resetSprites(self):
        boss.empty()
        enemies.empty()
        enemyLaserSprites.empty()
        laserSprites.empty()
        self.enemiesSpawned = 0
        player.dx = 0
        player.dy = 0

    def resetPowerups(self):
        self.laserMax = 20
        self.damage = 1
        self.shield = False


Run()
