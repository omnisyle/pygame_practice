import pygame

class EnemyExplosion(pygame.sprite.Sprite):

  def __init__(self, enemy, *groups):
    super(EnemyExplosion, self).__init__(*groups)
    self.image = self.get_image(enemy.enemyType, (40, 35))
    self.image2 = self.get_image(enemy.enemyType, (50, 45))
    self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y))
    self.timer = pygame.time.get_ticks()

  def get_image(self, enemy_type, scale):
    file_name = 'explosion{}'.format(enemy_type)
    img = pygame.image.load('images/' + file_name + '.png').convert_alpha()
    return pygame.transform.scale(img, scale)

  def update(self, current_time, window):
    passed = current_time - self.timer
    if passed <= 100:
      window.blit(self.image, self.rect)
    elif passed <= 200:
      window.blit(self.image2, (self.rect.x - 6, self.rect.y - 6))
    elif 400 < passed:
      self.kill()