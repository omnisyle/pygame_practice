import pygame
import sys

import grid
import cube
import food
import snake

pygame.init()

def hit_food(snake, food):
	snack_pos = food.position
	snake_head = snake.get_head()
	head_pos = snake_head.position
	return head_pos[0] == snack_pos[0] and head_pos[1] == snack_pos[1]

def main():
	width = 800
	height = 600
	gridColor = (43,43,43)
	frameRate = 10
	gridSize = 20
	gameOver = False

	window = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()

	ggrid = grid.Grid(gridSize, gridColor, width, height)
	my_snake = snake.Snake(3, (400, 300), gridSize)
	snack = food.Food(width, height, gridSize, (200, 300))

	while not gameOver:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					my_snake.move_left()

				elif event.key == pygame.K_RIGHT:
					my_snake.move_right()

				elif event.key == pygame.K_UP:
					my_snake.move_up()

				elif event.key == pygame.K_DOWN:
					my_snake.move_down()

		# check for game over

		if my_snake.has_hit_wall(width, height):
			gameOver = True

		# check collision between cube and snack
		if hit_food(my_snake, snack):
			snack.move_random()
			my_snake.eat()

		window.fill((0,0,0))
		my_snake.move()
		my_snake.draw(window)
		snack.draw(window)
		ggrid.draw(window)

		pygame.display.update()
		clock.tick(frameRate)

main()