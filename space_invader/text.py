import pygame

class Text(object):
  def __init__(self, size, message, color, xpos, ypos):
    self.font = pygame.font.Font("fonts/space_invaders.ttf", size)
    self.surface = self.font.render(message, True, color)
    self.rect = self.surface.get_rect(topleft=(xpos, ypos))

  def draw(self, surface):
    surface.blit(self.surface, self.rect)