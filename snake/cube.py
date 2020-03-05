import pygame

class Cube(object):
	def __init__(self, start, dirnx = 0, dirny= 0, color=(255,0,0), size=20):
		self.pos = start
		self.dirnx = dirnx
		self.dirny = dirny
		self.color = color
		self.size = size

	def move(self):
		self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

	def draw(self, surface):
		dis = self.size
		i = self.pos[0]
		j = self.pos[1]

		pygame.draw.rect(surface, self.color, (i, j, dis, dis))

class Snake(object):
	def __init__(self, color, pos):
		self.body = []
		self.turns = {}
		self.head = Cube(pos)
		self.body.append(self.head)
		self.dirnx = 0
		self.dirny = 1

	def move(self):
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT]:
						self.dirnx = -self.head.size
						self.dirny = 0

				elif keys[pygame.K_RIGHT]:
						self.dirnx = self.head.size
						self.dirny = 0

				elif keys[pygame.K_UP]:
						self.dirnx = 0
						self.dirny = -self.head.size

				elif keys[pygame.K_DOWN]:
						self.dirnx = 0
						self.dirny = self.head.size

			self.head.move(self.dirnx, self.dirny)


	def draw(self, surface):
		for _, c in enumerate(self.body):
			c.draw(surface)


