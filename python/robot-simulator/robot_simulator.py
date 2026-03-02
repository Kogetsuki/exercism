# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
  def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
    self.direction = direction
    self.coordinates = (x_pos, y_pos)
    
  def advance(self):
    x, y = self.coordinates

    # EAST
    if self.direction == 0:
      self.coordinates = (x + 1, y)
    # NORTH
    elif self.direction == 1:
      self.coordinates = (x, y + 1)
    # WEST
    elif self.direction == 2:
      self.coordinates = (x - 1, y)
    # SOUTH
    elif self.direction == 3:
      self.coordinates = (x, y - 1)
    else:
      raise ValueError("incorrect input direction")
      

  def move(self, movements):
    for movement in movements:
      if movement == 'A':
        self.advance()
      elif movement == 'L':
        self.direction = (self.direction + 1) % 4
      elif movement == 'R':
        self.direction = (self.direction - 1) % 4
      else:
        raise ValueError("incorrect input movement")
      