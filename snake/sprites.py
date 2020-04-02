import pygame

class SpriteSheet(object):
    def __init__(self, file_name):
      self.spritesheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, row, col):
      size = 64
      image = pygame.Surface((size, size))
      image.blit(self.spritesheet, (0, 0), (col * size, row*size, size, size))
      image = pygame.transform.scale(image, (20, 20))
      image.set_colorkey((0,0,0))
      return image