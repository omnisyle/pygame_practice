import pygame

class Grid(object):
	def __init__(self, size, color = (255, 255, 255), windowWidth=800, windowHeight=600):
		self.size = size
		self.color = color
		self.windowWidth = windowWidth
		self.windowHeight = windowHeight

	def draw(self, surface):
		self.drawRows(surface)
		self.drawColumns(surface)

	def drawRows(self, surface):
		rows = self.windowHeight // self.size
		y = 0
		for l in range(rows):
			y = y + self.size
			pygame.draw.line(surface, self.color, (0, y), (self.windowWidth, y))

	def drawColumns(self, surface):
		columns = self.windowWidth // self.size
		x = 0
		for l in range(columns):
			x = x + self.size
			pygame.draw.line(surface, self.color, (x,0), (x, self.windowHeight))