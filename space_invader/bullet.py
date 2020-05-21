import pygame

PLAYER_BULLET = "laser"

class Bullet(pygame.sprite.Sprite):
  def __init__(self, xpos, ypos, direction, speed, filename):
    super().__init__()
    self.image = pygame.image.load('images/' + filename + '.png').convert();
    self.rect = self.image.get_rect(topleft=(xpos, ypos));

    self.speed = speed
    self.direction = direction

  def update(self, *args):
    self.rect.y += self.speed * self.direction
    if self.rect.y < 15 or self.rect.y > 600:
      self.kill()

class PlayerBullet(Bullet):
  def __init__(self, player, speed):
    xpos = player.rect.x + 23
    ypos = player.rect.y + 5
    direction = -1
    super().__init__(xpos, ypos, direction, speed, PLAYER_BULLET)