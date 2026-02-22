def gamestate(board):
  x_count = sum(row.count('X') for row in board)
  o_count = sum(row.count('O') for row in board)
  
  if o_count > x_count:
    raise ValueError("Wrong turn order: O started")
  
  if x_count > o_count + 1:
    raise ValueError("Wrong turn order: X went twice")

  size = len(board)
  lines = []

  # Rows
  lines.extend(board)

  # Columns
  lines.extend([''.join(board[j][i] for j in range(size)) for i in range(size)])
  
  # Diagonals
  lines.append(''.join(board[i][i] for i in range(size)))
  lines.append(''.join(board[i][size - i - 1] for i in range(size)))

  winners = set()
  for line in lines:
    if len(set(line)) == 1 and line[0] in 'XO':
      winners.add(line[0])
      
  if len(winners) > 1:
    raise ValueError("Impossible board: game should have ended after the game was won")
  
  if winners:
    return 'win'
      
  if x_count + o_count == 9:
    return 'draw'

  return 'ongoing'