import re

class ConnectGame:
  def __init__(self, board):
    rows = [
      re.findall(r"[XO.]", line)
      for line in board.splitlines()
    ]

    self.board = [
      r
      for r in rows
      if r
    ]

    self.h = len(self.board)
    self.w = len(self.board[0]) if self.h else 0


  def get_neighbors(self, r, c):
    neighbors = [
      (0, -1), (0, 1),
      (-1, 0), (-1, 1),
      (1, 0), (1, -1)
    ]

    for dr, dc in neighbors:
      nr, nc = r + dr, c + dc
      if (
        0 <= nr < self.h and
        0 <= nc < self.w
      ):
        yield nr, nc


  def dfs(self, stack, player, goal):
    seen = set(stack)

    while stack:
      r, c = stack.pop()

      if goal(r, c):
        return True

      for nr, nc in self.get_neighbors(r, c):
        if (
          (nr, nc) not in seen and
          self.board[nr][nc] == player
        ):
          seen.add((nr, nc))
          stack.append((nr, nc))

    return False


  def get_winner(self):
    # X
    start = [
      (r, 0)
      for r in range(self.h)
      if self.board[r][0] == "X"
    ]

    if self.dfs(
      start,
      "X",
      lambda r, c: c == self.w - 1
    ):
      return "X"

    # O
    start = [
      (0, c)
      for c in range(self.w)
      if self.board[0][c] == "O"
    ]

    if self.dfs(
      start,
      "O",
      lambda r, c: r == self.h - 1
    ):
      return "O"

    return ""
