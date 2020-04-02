import cube

class Snake(object):

  def __init__(self, length, start, grid_size, sprite, color = (255,0,0)):
    self.dirnx = 0
    self.dirny = 0
    self.color = color
    self.body = []
    self.direction = "left"
    self.grid_size = grid_size
    self.sprite = sprite

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
    print(self.body)
    for i, segment in enumerate(self.body):
      seg_pos = segment.position
      segx = seg_pos[0]
      segy = seg_pos[1]

      row = 0
      col = 0

      if (i == 0):
        # Head; Determine the correct image
        nseg = self.body[i+1] # Next segment
        nsegx = nseg.position[0]
        nsegy = nseg.position[1]

        if (segy < nsegy):
          # Up
          col = 3; row = 0
        elif (segx > nsegx):
          # Right
          col = 4; row = 0
        elif (segy > nsegy):
          # Down
          col = 4; row = 1
        elif (segx < nsegx):
          # Left
          col = 3; row = 1

      if (i == len(self.body) - 1):
        # Tail; Determine the correct image
        pseg = self.body[i-1] # Prev segment
        psegx = pseg.position[0]
        psegy = pseg.position[1]

        if (psegy < segy):
          # Up
          col = 3; row = 2
        elif (psegx > segx):
          # Right
          col = 4; row = 2
        elif (psegy > segy):
          # Down
          col = 4; row = 3
        elif (psegx < segx):
          # Left
          col = 3; row = 3

      if (i > 0 and i < (len(self.body) - 1)):
        # Body; Determine the correct image
        # Previous segment
        pseg = self.body[i-1]
        psegx = pseg.position[0]
        psegy = pseg.position[1]

        # Next segment
        nseg = self.body[i+1]
        nsegx = nseg.position[0]
        nsegy = nseg.position[1]

        if (psegx < segx and nsegx > segx or nsegx < segx and psegx > segx):
            # Horizontal Left-Right
            col = 1; row = 0
        elif (psegx < segx and nsegy > segy or nsegx < segx and psegy > segy):
            # Angle Left-Down
            col = 2; row = 0
        elif (psegy < segy and nsegy > segy or nsegy < segy and psegy > segy):
            # Vertical Up-Down
            col = 2; row = 1
        elif (psegy < segy and nsegx < segx or nsegy < segy and psegx < segx):
            # Angle Top-Left
            col = 2; row = 2
        elif (psegx > segx and nsegy < segy or nsegx > segx and psegy < segy):
            # Angle Right-Up
            col = 0; row = 1
        elif (psegy > segy and nsegx > segx or nsegy > segy and psegx > segx):
            # Angle Down-Right
            col = 0; row = 0

      image = self.sprite.get_image(row, col)
      segment.draw_image(surface, image)

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