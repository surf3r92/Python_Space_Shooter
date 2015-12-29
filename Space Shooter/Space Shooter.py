import os, sys, pygame, random
from pygame.locals import *
os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("Space Shooter.png")
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Arena (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/arena.jpg", -1)
        self.dy = 3
        self.reset()

    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1200:
            self.reset()

    def reset(self):
        self.rect.top = -600


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/ship.png", -1)
        self.rect.center = (400, 500)
        self.dx = 0
        self.dy = 0
        self.laserTimer = 0
        self.laserMax = 5
        self.reset()

    def update(self):
        self.rect.move_ip((self.dx, self.dy))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.laserTimer += 1
            if self.laserTimer == self.laserMax:
                laserSprites.add(Laser(self.rect.midtop))
                self.laserTimer = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 260:
            self.rect.top = 260
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

    def reset(self):
        self.rect.bottom = 600


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/laser.png", -1)
        self.rect.center = pos

    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:
            self.rect.move_ip(0, -15)


def game():

    # Game Objects
    global player
    player = Player()

    playerSprite = pygame.sprite.RenderPlain((player))

    # Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))

    # Projectiles
    global laserSprites
    laserSprites = pygame.sprite.RenderPlain()

    clock = pygame.time.Clock()
    keepgoing = True
    counter = 0
    pygame.key.set_repeat(10, 10)
    while keepgoing:
        clock.tick(30)
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                keepgoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepgoing = False
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
        screen.blit(background, (0, 0))
        playerSprite.update()
        arena.update()
        laserSprites.update()

        # Draw
        arena.draw(screen)
        playerSprite.draw(screen)
        laserSprites.draw(screen)
        pygame.display.flip()


def main():
    arena = Arena()


game()