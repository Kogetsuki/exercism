def get_neighbors(matrix, row_i, col_i):
  total_rows = len(matrix)
  total_cols = len(matrix[0])

  offsets = [
    (-1, -1), # up left
    (-1, 0),  # up
    (-1, 1),  # up right
    (0, -1),  # left
    (0, 1),   # right
    (1, -1),  # down left
    (1, 0),   # down
    (1, 1)    # down right
  ]
  
  neighbors = []

  for row_o, col_o in offsets:
    neighbor_row = row_i + row_o
    neighbor_col = col_i + col_o
    
    is_valid_row = 0 <= neighbor_row < total_rows
    is_valid_col = 0 <= neighbor_col < total_cols
    
    if is_valid_row and is_valid_col:
      neighbors.append(matrix[neighbor_row][neighbor_col])
      
  return neighbors


def get_new_state(matrix, i, j):
  total = sum(get_neighbors(matrix, i, j))
  return (
    matrix[i][j] and (total == 2 or total == 3) or
    not matrix[i][j] and total == 3
  )

def tick(matrix):
  result = [
    [None] * len(matrix)
    for _ in range(len(matrix))
  ]
  
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      result[i][j] = int(get_new_state(matrix, i, j))
      
  return result
