import pygame

class Cube(object):
	def __init__(self, start, color=(255,0,0), size=20):
		self.position = start
		self.color = color
		self.size = size

	def draw(self, surface):
		dis = self.size
		i = self.position[0]
		j = self.position[1]

		pygame.draw.rect(surface, self.color, (i, j, dis, dis))

	def __str__(self):
		return 'Cube("%s","%s")' % (self.position[0], self.position[1])

	def __repr__(self):
		return 'Cube("%s","%s")' % (self.position[0], self.position[1])