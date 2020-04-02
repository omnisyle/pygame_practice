import pygame
import random
import cube

class Food(object):
  def __init__(self, window_width, window_height, grid_size, sprite, position = (0,0), color = (0, 255, 0), ):
    self.window_width = window_width
    self.window_height = window_height
    self.grid_size = grid_size
    self.position = position
    self.color = color
    self.snack = cube.Cube(self.position, color, grid_size)
    self.image = sprite.get_image(3, 0)

  def move_random(self):
    snackx = random.randrange(0, self.window_width, self.grid_size)
    snacky = random.randrange(0, self.window_height, self.grid_size)
    self.position = (snackx, snacky)
    self.snack.position = self.position

  def draw(self, surface):
    self.snack.draw_image(surface, self.image)