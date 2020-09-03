import pygame

class Life(pygame.sprite.Sprite):
  def __init__(self, xpos, ypos):
    super().__init__()
    self.image = pygame.image.load("images/ship.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (23, 23))
    self.rect = self.image.get_rect(topleft=(xpos, ypos))

  def update(self):
    pass