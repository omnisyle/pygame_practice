import pygame
import sys
from os.path import abspath, dirname

from ship import *
from bullet import PlayerBullet, EnemyBullet
from enemy import EnemyGroup
from text import Text
from wall_sprite import WallSprite
from enemy_explosion import EnemyExplosion

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
    right_edge = WallSprite(10, 600, (790,0))
    left_edge = WallSprite(10, 600, (0,0))
    self.edgesGroup = pygame.sprite.Group(left_edge, right_edge)
    self.allSprites = pygame.sprite.Group(self.player, self.edgesGroup)
    self.bullets = pygame.sprite.Group()
    self.enemy_bullets = pygame.sprite.Group()
    self.shipAlive = True
    self.total_score = 0
    self.sounds = self.create_audio()
    self.level = 1
    self.enemy_explosions_group = pygame.sprite.Group()
    self.enemies = None
    self.enemy_bullet_timer = pygame.time.get_ticks()
    self.score_text = Text(20, 'Score   ' + str(self.total_score), (255,255,255), 5, 5)

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
      20,
      600,
      15,
      10,
    )
    self.allSprites.add(self.enemies)

  def shoot_player_bullets(self):
    if len(self.bullets) == 0 and self.shipAlive:
      playerBullet = PlayerBullet(self.player, 15)
      self.bullets.add(playerBullet)
      self.allSprites.add(self.bullets)
      self.sounds['shoot'].play()

  def detect_enemy_hit(self):
    enemies_bullets_killed = pygame.sprite.groupcollide(
        self.enemies,
        self.bullets,
        True,
        True)

    if (bool(enemies_bullets_killed)):

      for enemy in enemies_bullets_killed:
        self.total_score += enemy.score
        self.score_text = Text(20, 'Score   ' + str(self.total_score), (255,255,255), 5, 5)
        EnemyExplosion(enemy, self.enemy_explosions_group)

      print("Total score", self.total_score)
      self.sounds['invaderkilled'].play()

  def shoot_enemy_bullets(self):
    current_time = pygame.time.get_ticks()
    if (current_time - self.enemy_bullet_timer) > 700 and self.enemies and len(self.enemies) > 0:
      enemy = self.enemies.random_enemy()
      self.enemy_bullets.add(EnemyBullet(enemy, 10))
      self.allSprites.add(self.enemy_bullets)
      self.enemy_bullet_timer = pygame.time.get_ticks()

  def detect_player_hit(self):
    player_hit = pygame.sprite.spritecollide(
        self.player,
        self.enemy_bullets,
        False)

    if (bool(player_hit)):
      print("Player hit")
      self.sounds['shipexplosion'].play()

  def main(self):
    self.make_enemies()

    while True:
      for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.KEYDOWN:
          if e.key == pygame.K_SPACE:
            self.shoot_player_bullets()

      self.detect_enemy_hit()
      self.shoot_enemy_bullets()
      self.detect_player_hit()

      current_time = pygame.time.get_ticks()

      # draw background
      self.screen.blit(self.background, (0,0))

      # draw enemies
      self.enemies.update(current_time, self.edgesGroup)

      # draw enemy explosions
      self.enemy_explosions_group.update(current_time, self.screen)

      self.score_text.draw(self.screen)
      self.allSprites.update()
      self.allSprites.draw(self.screen)
      pygame.display.update()
      self.clock.tick(60)


game = SpaceInvader()
game.main()