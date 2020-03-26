import cube

class Snake(object):

  def __init__(self, length, start, grid_size, color = (255,0,0)):
    self.dirnx = 0
    self.dirny = 0
    self.color = color
    self.body = []
    self.direction = "left"
    self.grid_size = grid_size

    for x in range(length):
      count = x + 1
      segment_position = [start[0] + (grid_size * count), start[1]]
      segment = cube.Cube(
        segment_position,
        color,
        grid_size
      )
      self.body.append(segment)

  def move_right(self):
    if self.direction == "left":
      return
    self.dirnx = self.grid_size
    self.dirny = 0
    self.direction = "right"

  def move_left(self):
    if self.direction == "right":
      return

    self.dirnx = -self.grid_size
    self.dirny = 0
    self.direction = "left"

  def move_up(self):
    if self.direction == "down":
      return

    self.dirnx = 0
    self.dirny = -self.grid_size
    self.direction = "up"

  def move_down(self):
    if self.direction == "up":
      return

    self.dirnx = 0
    self.dirny = self.grid_size
    self.direction = "down"

  def move(self):
    if self.dirnx == 0 and self.dirny == 0:
      return

    snake_head = self.make_new_head()
    self.body.insert(0, snake_head)
    self.body.pop()

  def draw(self, surface):
    for segment in self.body:
      segment.draw(surface)

  def has_hit_wall(self, width, height):
    head_position = self.body[0].position
    return head_position[0] < 0 \
      or head_position[0] > width \
      or head_position[1] > height \
      or head_position[1] < 0

  def get_head(self):
    return self.body[0]

  def eat(self):
    new_head = self.make_new_head()
    self.body.insert(0, new_head)

  def make_new_head(self):
    current_head = self.get_head().position
    new_head_position = (current_head[0] + self.dirnx, current_head[1] + self.dirny)
    snake_head = cube.Cube(
      new_head_position,
      self.color,
      self.grid_size
    )

    return snake_head