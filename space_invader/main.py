import pygame
import sys
from os.path import abspath, dirname

from ship import *
from bullet import *
from enemy import EnemyGroup

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

LEVELS = {
  1: [
    [None, 'purple', 'purple', 'purple'],
    ['green', 'purple', 'green', 'purple'],
    ['green', 'teal', 'green', 'purple'],
    ['green', None, 'green', None],
    ['green', 'purple', 'green', 'purple'],
  ]
}

class SpaceInvader(object):
  def __init__(self):
    pygame.init()
    pygame.mixer.init()

    self.screen = SCREEN
    self.game_over = False
    self.clock = pygame.time.Clock()
    self.background = pygame.image.load(IMAGE_PATH + 'background.jpg').convert()
    self.player = Ship()
    self.allSprites = pygame.sprite.Group(self.player)
    self.bullets = pygame.sprite.Group()
    self.shipAlive = True
    self.sounds = self.create_audio()
    self.level = 1

  def create_audio(self):
    sounds = {}
    sfx = ['shoot', 'shoot2', 'invaderkilled', 'mysterykilled', 'shipexplosion']
    for sound_name in sfx:
      sounds[sound_name] = pygame.mixer.Sound(
        'sounds/' + sound_name + '.wav'
      )
      sounds[sound_name].set_volume(0.2)

    return sounds

  def make_enemies(self):
    level = LEVELS[self.level]
    self.enemies = EnemyGroup(
      (65, 30),
      level,
      10,
      600,
      15,
      10,
    )
    self.allSprites.add(self.enemies)

  def main(self):
    while True:
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_SPACE:
            if len(self.bullets) == 0 and self.shipAlive:
              playerBullet = PlayerBullet(self.player, 15)
              self.bullets.add(playerBullet)
              self.allSprites.add(self.bullets)
              self.sounds['shoot'].play()

          if e.key == pygame.K_SEMICOLON:
            self.make_enemies()


      self.screen.blit(self.background, (0,0))
      self.allSprites.update()
      self.allSprites.draw(self.screen)
      pygame.display.update()
      self.clock.tick(60)


game = SpaceInvader()
game.main()