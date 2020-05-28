import pygame

ENEMY_FILES = {
  "purple": ["enemy1_1", "enemy1_2"],
  "teal": ["enemy2_1", "enemy2_2"],
  "green": ["enemy3_1", "enemy3_2"],
}

ENEMY_SCORES = {
  "purple": 30,
  "teal": 20,
  "green": 10
}

ENEMY_SIZE = (40, 35)

class Enemy(pygame.sprite.Sprite):

  def __init__(self, enemyType):
    super().__init__()
    self.enemyType = enemyType
    self.score = ENEMY_SCORES[enemyType]
    self.images = self.load_images(ENEMY_FILES[enemyType])
    self.index = 0
    self.image = self.images[0]
    self.rect = self.image.get_rect()

  def toggle_image(self):
    self.index += 1
    if self.index >= len(self.images):
        self.index = 0
    self.image = self.images[self.index]

  def load_images(self, fileNames):
    images = []
    for fileName in fileNames:
      image = pygame.image.load('images/' + fileName + '.png').convert_alpha()
      scaled_image = pygame.transform.scale(image, ENEMY_SIZE)
      images.append(scaled_image)

    return images

  def move(self, x, y):
    self.rect.x += x
    self.rect.y += y

  def set_position(self, x, y):
    self.rect.x = x
    self.rect.y = y

  def set_grid_position(self, row, column):
    self.row = row
    self.column = column

class EnemyGroup(pygame.sprite.Group):
  def __init__(self, start_position, enemy_map, velocity, move_time, x_gutter, y_gutter):
    super().__init__()
    self.rows = len(enemy_map)
    # assuming all rows has the same number of columns
    self.columns = len(enemy_map[0])

    # make enemies grid
    self.enemies = [[None] * self.columns for _ in range(self.rows)]

    self.start_position = start_position
    self.timer = pygame.time.get_ticks()
    self.enemy_map = enemy_map
    self.velocity = velocity
    self.move_time = move_time
    self.y_gutter = y_gutter
    self.x_gutter = x_gutter
    self.direction = 1

    self.init_enemies()

  def init_enemies(self):
    grid_pointer = self.start_position
    for row in range(len(self.enemy_map)):
      enemyRow = self.enemy_map[row]

      for column in range(len(enemyRow)):
        enemyType = enemyRow[column]

        if enemyType is not None:
          enemy = Enemy(enemyType)

          enemy.set_grid_position(row, column)
          enemy.set_position(grid_pointer[0], grid_pointer[1])
          self.enemies[row][column] = enemy
          self.add(enemy)

        # keep y position constant and move x position
        xpos = self.start_position[0] + ENEMY_SIZE[0] * (column + 1)
        if column < len(enemyRow):
            xpos += (self.x_gutter * (column + 1))

        grid_pointer = (xpos, grid_pointer[1])

      # reset pointer to initial x position and move y position down
      xpos = self.start_position[0]
      ypos = self.start_position[1] + ENEMY_SIZE[1] * (row + 1)
      if row < len(self.enemy_map):
        ypos += (self.y_gutter * (row + 1))
      grid_pointer = (xpos, ypos)

  def update(self, current_time):
    if (current_time - self.timer) > self.move_time:
      velocity = self.velocity * self.direction
      for enemy in self:
        enemy.move(velocity, 0)
        enemy.toggle_image()

      self.timer += self.move_time