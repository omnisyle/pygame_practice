import cube
import random

class Snack(object):
  def __init__(self, surfaceWidth, surfaceHeight, size, color=(255, 255, 255)):
    self.windowWidth = surfaceWidth
    self.windowHeight = surfaceHeight
    self.size = size
    self.color = color
    self.cube = cube.Cube((0,0), 0, 0, color, size)

  def drawRand(self, surface, pos):
