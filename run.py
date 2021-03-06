import os, sys, pygame, random
from pygame.locals import *
from lib.highscore import *
from lib.arena import arena
from lib.player import *
from lib.enemy import *
from lib.powerup import *
from lib.menu import *
from lib.boss import *
from lib.explosion import *


class Run():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = "1"
        pygame.init()
        pygame.display.set_caption("Space Shooter")

        self.icon = pygame.image.load("img/sprites/Space Shooter.png")
        self.playerLivesPictures = pygame.image.load("img/sprites/player.png")
        self.blue = 0, 194, 244
        self.score = 0
        self.highscoreList = open("csv/highscore.csv").read().split()
        self.lives = 3

        self.fontLink = "fonts/orbitron-light.otf"

        self.enemiesSpawned = 0
        self.level = 0

        self.myFont = pygame.font.Font(self.fontLink, 24)
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
        self.multipleShoot = 1
        self.shieldTime = 0
        self.shieldStatus = False
        self.additionalMovementSpeed = 0
        self.fasterMovementTime = 0
        self.fasterMovementStatus = False

        self.powerupShieldCountDownLength = 202.0
        self.powerupFasterMovementCountDownLength = 202.0
        self.powerupShieldCountDownStartLength = 200.0
        self.powerupFasterMovementCountDownStartLength = 200.0

        self.playerExplosionImages = []
        for i in range(1, 18):
            self.playerExplosionImages.append(load_image("img/sprites/Blue Explosion/" + str(i) + ".png", -1))

        self.explosionCounter = 0
        self.explosionPosition = (0, 0)
        self.explosionTime = 20
        self.explosionStatus = False
        self.deleteShip = False
        self.currentExplosionImage = load_image("img/sprites/Blue Explosion/1.png", -1)


        global player
        player = Player()

        global playerSprite
        playerSprite = pygame.sprite.RenderPlain((player))

        global explosion
        explosion = Explosion(player.getPos())

        global explosionSprite
        explosionSprite = pygame.sprite.RenderPlain((explosion))

        gameMenu(self)

    def callHighscore(self):
        highScore(self)

    def callGame(self):
        self.game()

    def game(self):

        self.livesImage, self.livesRect = load_image("img/sprites/ship.png", -1)
        self.livesImage = pygame.transform.scale(self.livesImage,
                                                 (int(self.livesImage.get_width()*0.75),
                                                  int(self.livesImage.get_height()*0.75)))

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
                    randomInt = random.randint(0, 4)
                    if randomInt == 0:
                        self.randomPowerup = "fasterLaser"
                    elif randomInt == 1:
                        self.randomPowerup = "health"
                    elif randomInt == 2:
                        self.randomPowerup = "shield"
                    elif randomInt == 3:
                        self.randomPowerup = "multipleShoot"
                    elif randomInt == 4:
                        self.randomPowerup = "fasterMovement"

                    laserPowerups.add(Powerup((self.xPowerups, -20), self.randomPowerup))

                if self.shieldStatus:
                    self.shieldTime += 1
                    self.powerupShieldCountDownLength -= self.powerupShieldCountDownStartLength / 150
                if self.fasterMovementStatus:
                    self.fasterMovementTime += 1
                    self.powerupFasterMovementCountDownLength -= self.powerupFasterMovementCountDownStartLength / 250

                if self.explosionStatus:
                    if self.explosionTime == 20:
                        self.explosionPosition = player.getPos()
                        explosionSprite.update(self.explosionPosition)
                    self.explosionTime += 1
                    if self.explosionTime % 3 == 0:
                        self.explosionCounter += 1
                        if self.explosionCounter < 17:
                            self.currentExplosionImage = self.playerExplosionImages[self.explosionCounter]
                            changeImage(self.currentExplosionImage, explosionSprite)
                            if self.explosionCounter == 1:
                                player.rect.center = (1000, 1000)
                        else:
                            self.gameState = "Gameover"

                if len(boss.sprites()) == 1:
                    if boss.sprites()[0].health <= 0:
                        boss.sprites()[0].kill()
                        self.score += 1000
                        self.nextLevel()

                if frameCounter % (70 - self.level*2) == 0 and frameCounter > 200:
                    meteorites.add(Meteorite((random.randint(10,790), -100)))
                if frameCounter % (1000 - self.level*20) == 400 and frameCounter > 200:
                    for i in range(0,20):
                        meteorites.add(Meteorite((random.randint(10,790), random.randint(0, 1500)*-1)))

                if self.enemiesSpawned < (20 + self.level*10):
                    if frameCounter % 200 == 1 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(0, 8) * 100 - 50
                        if self.xGroup <= 50:
                            self.enemyY = 300
                            self.xGroup = - 20
                        elif self.xGroup >= 650:
                            self.enemyY = 300
                            self.xGroup = self.width + 20
                        else:
                            self.enemyY = -20
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 200 == 21 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 200 == 41 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 200 == 61 and frameCounter > 200:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 400 == 81 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        self.xGroup = random.randint(1, 7) * 100 - 50
                        if self.xGroup <= 50:
                            self.enemyY = 300
                            self.xGroup = - 20
                        elif self.xGroup >= 650:
                            self.enemyY = 300
                            self.xGroup = self.width + 20
                        else:
                            self.enemyY = -20
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 400 == 101 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 400 == 121 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))

                    if frameCounter % 400 == 141 and frameCounter > 400:
                        self.enemiesSpawned += 1
                        enemies.add(Enemy((self.xGroup, self.enemyY)))
                elif len(enemies.sprites()) == 0 and len(boss.sprites()) == 0:
                    boss.add(Boss((self.width/2, -50)))
                    boss.sprites()[0].health = 20 + self.level*10

                keyControls(self, player, self.additionalMovementSpeed)

                # Update
                playerSprite.update(self.multipleShoot, self.explosionStatus)
                arena.update(self.screen)
                laserSprites.update()
                bossLaserSprites.update()
                enemies.update()
                enemyLaserSprites.update()
                boss.update()
                meteorites.update()
                laserPowerups.update()
                explosionSprite.update(self.explosionPosition)

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

                scoreDisplay = self.myFont.render("".join(["Score: ", str(self.score)]), 1, self.blue)
                self.screen.blit(scoreDisplay, (self.width - 200, self.height - 40))

                if self.shieldStatus == True:
                    powerupCountDownHeight = 15
                    pygame.draw.rect(self.screen, (250,223,76), (self.width/2, self.height - 45, self.powerupShieldCountDownLength, powerupCountDownHeight), 0)

                if self.fasterMovementStatus == True:
                    powerupCountDownHeight = 15
                    pygame.draw.rect(self.screen, (70,250,60), (self.width/2, self.height - 25, self.powerupFasterMovementCountDownLength, powerupCountDownHeight), 0)

                boss_hit = pygame.sprite.groupcollide(laserSprites, boss, True, False)
                if boss_hit != {}:
                    if boss.sprites()[0].invincible == 0:
                        boss.sprites()[0].health -= self.multipleShoot

                collide_Laser_Enemy = pygame.sprite.groupcollide(laserSprites, enemies, True, True)
                if collide_Laser_Enemy != {}:
                    self.score += 10 + self.level*5

                collide_Meteorite = pygame.sprite.spritecollide(player, meteorites, True)

                collide_Boss_Laser = pygame.sprite.spritecollide(player, bossLaserSprites, True)

                collide_Player_Laser = pygame.sprite.spritecollide(player, enemyLaserSprites, True)
                if len(collide_Player_Laser) and self.shieldStatus == False:
                    self.lives -= 1
                    self.resetPowerups()

                if len(collide_Meteorite) and self.shieldStatus == False:
                    self.lives -= 1
                    self.resetPowerups()
                    
                if len(collide_Boss_Laser) and self.shieldStatus == False:
                    self.lives -= 1
                    self.resetPowerups()

                if self.lives <= 0:
                    self.explosionStatus = True
                    if self.explosionCounter >= len(self.playerExplosionImages)-1:
                        self.gameState = "Gameover"
                        updateHighscore(self, self.currUserName, self.score)
                        gameMenu(self)

                collide_Player_Enemy = pygame.sprite.spritecollide(player, enemies, True)
                if len(collide_Player_Enemy) and self.shieldStatus == False:
                    self.lives -= 1
                    self.resetPowerups()

                powerup_collected = pygame.sprite.spritecollide(player, laserPowerups, True)
                if len(powerup_collected):
                    self.score += 50
                    if self.randomPowerup == "fasterLaser":
                       player.increaseLaserSpeed()
                    elif self.randomPowerup == "health":
                        if self.lives < 5:
                            self.lives += 1
                        elif self.lives > 4:
                            pass
                    elif self.randomPowerup == "multipleShoot":
                        self.multipleShoot += 1
                    elif self.randomPowerup == "shield":
                        activateShield(playerSprite)
                        self.shieldTime = 0
                        self.powerupShieldCountDownLength = self.powerupShieldCountDownStartLength
                        self.shieldStatus = True
                    elif self.randomPowerup == "fasterMovement":
                        self.additionalMovementSpeed = 5
                        self.fasterMovementTime = 0
                        self.powerupFasterMovementCountDownLength = self.powerupFasterMovementCountDownStartLength
                        self.fasterMovementStatus = True

                if self.shieldTime > 150:
                    deActivateShield(playerSprite)
                    self.shieldTime = 0
                    self.powerupShieldCountDownLength = self.powerupShieldCountDownStartLength
                    self.shieldStatus = False

                if self.fasterMovementTime > 250:
                    self.additionalMovementSpeed = 0
                    self.powerupFasterMovementCountDownLength = self.powerupFasterMovementCountDownStartLength
                    self.fasterMovementStatus = False

                playerSprite.draw(self.screen)
                laserSprites.draw(self.screen)
                bossLaserSprites.draw(self.screen)
                enemies.draw(self.screen)
                enemyLaserSprites.draw(self.screen)
                boss.draw(self.screen)
                meteorites.draw(self.screen)
                laserPowerups.draw(self.screen)

                if self.explosionStatus:
                    explosionSprite.draw(self.screen)

                for i in range(0, self. lives):
                    self.screen.blit(self.livesImage, (8 + i*self.livesImage.get_width()*1.5, self.height -
                                                       self.livesImage.get_height()-8))
                pygame.display.flip()

    def nextLevel(self):
        self.resetSprites()
        self.level += 1
        self.game()

    def setupNewGame(self):
        self.explosionTime = 20
        self.explosionCounter = 0
        meteorites.empty()
        self.explosionStatus = False
        self.additionalMovementSpeed = 0
        self.shieldStatus = False
        deActivateShield(playerSprite)
        player.rect.center = (400, 500)
        self.resetPowerups()
        self.resetSprites()
        laserPowerups.empty()
        self.lives = 3
        self.score = 0
        self.level = 1
        self.game()

    def resetSprites(self):
        meteorites.empty()
        boss.empty()
        bossLaserSprites.empty()
        enemies.empty()
        enemyLaserSprites.empty()
        laserSprites.empty()
        self.enemiesSpawned = 0
        player.dx = 0
        player.dy = 0

    def resetPowerups(self):
        self.fasterMovementStatus = False
        self.shieldStatus = False
        self.additionalMovementSpeed = 0
        self.multipleShoot = 1
        player.resetLaser()

#start game
Run()
