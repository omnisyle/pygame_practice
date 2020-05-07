import pygame
from os.path import abspath, dirname

BASE_PATH = abspath(dirname(__file__))
IMAGE_PATH = BASE_PATH + '/images/'

class Ship(pygame.sprite.Sprite):
  def __init__(self, screen):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(IMAGE_PATH + 'ship.png').convert_alpha()
    self.rect = self.image.get_rect(topleft=(375,540))
    self.screen = screen
    self.speed = 5

  def update(self, keys, *args):
    if keys[pygame.K_LEFT] and self.rect.x > 10:
      self.rect.x -= self.speed

    if keys[pygame.K_RIGHT] and self.rect.x < 740:
      self.rect.x += self.speed
    self.screen.blit(self.image, self.rect)
