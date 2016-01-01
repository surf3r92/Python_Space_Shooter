import os, sys, pygame, random
from pygame.locals import *
from lib.arena import *
from lib.player import *
from lib.menu import *

os.environ['SDL_VIDEO_CENTERED'] = "1"
pygame.init()
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("img/sprites/Space Shooter.png")
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)


background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))


def game():

    # Game Objects
    global player
    player = Player()

    playerSprite = pygame.sprite.RenderPlain((player))

    # Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))

    # Projectiles


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


#game()

def main():

   # Create 3 diffrent menus.  One of them is only text, another one is only
   # images, and a third is -gasp- a mix of images and text buttons!  To
   # understand the input factors, see the menu file
   menu = cMenu(50, 50, 20, 10, 'vertical', 100, screen,
               [('Start Game', 1, None),
                ('Load Game',  2, None),
                ('Options',    3, None),
                ('Exit',       4, None)])

   menu.set_center(True, True)
   menu.set_alignment('center', 'center')

   state = 0
   prev_state = 1

   rect_list = []

   #pygame.event.set_blocked(pygame.MOUSEMOTION)

   while 1:
      if prev_state != state:
         pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
         if state == 0:
            rect_list, state = menu.update(e, state)
         elif state == 1:
            print 'Start Game!'
            state = 0
            game()
         elif state == 2:
            print 'Load Game!'
            state = 0
         elif state == 3:
            print 'Options!'
            state = 0
         else:
            print 'Exit!'
            pygame.quit()
            sys.exit()

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      # Update the screen
      pygame.display.update(rect_list)

main()