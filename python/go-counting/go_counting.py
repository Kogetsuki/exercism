
WHITE = "W"
BLACK = "B"
NONE = ""

class Board:
  """Count territories of each player in a Go game

  Args:
      board (list[str]): A two-dimensional Go board
  """

  def __init__(self, board):
    self.board = board
    self.height = len(board)
    self.width = len(board[0])


  def is_in_bounds(self, x, y):
    return (
      0 <= x < self.width and
      0 <= y < self.height
    )


  def get_neighbors(self, x, y):
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in neighbors:
      nx, ny = x + dx, y + dy
      if self.is_in_bounds(nx, ny):
        yield nx, ny


  def territory(self, x, y):
    """Find the owner and the territories given a coordinate on
       the board

    Args:
        x (int): Column on the board
        y (int): Row on the board

    Returns:
        (str, set): A tuple, the first element being the owner
                    of that area.  One of "W", "B", "".  The
                    second being a set of coordinates, representing
                    the owner's territories.
    """
    if not self.is_in_bounds(x, y):
      raise ValueError("Invalid coordinate")

    if self.board[y][x] != " ":
      return NONE, set()

    stack = [(x, y)]
    visited = set()
    borders = set()

    while stack:
      cx, cy = stack.pop()

      if (cx, cy) in visited:
        continue

      visited.add((cx, cy))

      for nx, ny in self.get_neighbors(cx, cy):
        val = self.board[ny][nx]

        if val == " ":
          stack.append((nx, ny))
        else:
          borders.add(val)

    if borders == {BLACK}:
      owner = BLACK
    elif borders == {WHITE}:
      owner = WHITE
    else:
      owner = NONE

    return owner, visited




  def territories(self):
    """Find the owners and the territories of the whole board

    Args:
        none

    Returns:
        dict(str, set): A dictionary whose key being the owner
                    , i.e. "W", "B", "".  The value being a set
                    of coordinates owned by the owner.
    """
    visited = set()
    result = {
      BLACK: set(),
      WHITE: set(),
      NONE: set()
    }

    for y in range(self.height):
      for x in range(self.width):
        if self.board[y][x] != " " or (x, y) in visited:
          continue

        owner, region = self.territory(x, y)
        visited.update(region)
        result[owner].update(region)

    return result
