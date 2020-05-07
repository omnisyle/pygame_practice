import pygame
import sys
from os.path import abspath, dirname

from ship import *

BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/fonts/'
IMAGE_PATH = BASE_PATH + '/images/'
SOUND_PATH = BASE_PATH + '/sounds/'

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

class SpaceInvader(object):
  def __init__(self):
    pygame.init()

    self.screen = SCREEN
    self.game_over = False
    self.clock = pygame.time.Clock()
    self.background = pygame.image.load(IMAGE_PATH + 'background.jpg').convert()
    self.player = Ship()
    self.allSprites = pygame.sprite.Group(self.player)

  def main(self):
    while True:
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

      self.screen.blit(self.background, (0,0))
      self.allSprites.update()
      self.allSprites.draw(self.screen)
      pygame.display.update()
      self.clock.tick(60)


game = SpaceInvader()
game.main()