import pygame

class WallSprite(pygame.sprite.Sprite):
  def __init__(self, width, height, position):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill((255,0,0))
    self.rect = self.image.get_rect(topleft=position)

  def update(self):
    pass