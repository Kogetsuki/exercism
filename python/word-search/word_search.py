class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


class WordSearch:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.rows = len(puzzle)
    self.cols = len(puzzle[0])


  DIRECTIONS = [
    (0, -1),     # left
    (0, 1),      # right
    (-1, 0),     # up
    (1, 0),      # down
    (-1, -1),    # up left
    (-1, 1),     # up right
    (1, -1),     # down left
    (1, 1),      # down right
  ]


  def search(self, word):
    for r in range(self.rows):
      for c in range(self.cols):
        for dr, dc in self.DIRECTIONS:
          result = self.check_direction(word, r, c, dr, dc)
          if result:
            return result

    return None


  def check_direction(self, word, start_r, start_c, dr, dc):
    r, c = start_r, start_c

    for letter in word:
      if not (0 <= r < self.rows and 0 <= c < self.cols):
        return None

      if self.puzzle[r][c] != letter:
        return None

      r += dr
      c += dc

    start = Point(start_c, start_r)
    end = Point(c - dc, r - dr)

    return (start, end)
