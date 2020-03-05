import pygame
import sys

import grid
import cube

pygame.init()

def main():
	width = 800
	height = 600
	gridColor = (43,43,43)
	frameRate = 20
	gridSize = 15
	gameOver = False

	window = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()

	ggrid = grid.Grid(gridSize, gridColor, width, height)
	ccube = cube.Cube((0,0), 0, 0, (255,0,0), gridSize)
	#snake = Snake((255,0,0), (0,0))

	while not gameOver:

		# snake.move()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					ccube.dirnx = -gridSize
					ccube.dirny = 0

				elif event.key == pygame.K_RIGHT:
					ccube.dirnx = gridSize
					ccube.dirny = 0

				elif event.key == pygame.K_UP:
					ccube.dirnx = 0
					ccube.dirny = -gridSize

				elif event.key == pygame.K_DOWN:
					ccube.dirnx = 0
					ccube.dirny = gridSize

		cube_pos = ccube.pos
		if cube_pos[0] < 0 or cube_pos[0] > width or cube_pos[1] > height or cube_pos[1] < 0:
			gameOver = True

		window.fill((0,0,0))
		ccube.move()
		ccube.draw(window)
		ggrid.draw(window)
		#snake.draw(window)

		pygame.display.update()
		clock.tick(frameRate)

main()