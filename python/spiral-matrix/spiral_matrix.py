def spiral_matrix(size):
  matrix = [[0] * size for _ in range(size)]
  
  top, bottom = 0, size - 1
  left, right = 0, size - 1
  x = 1
  
  while x <= size * size:
    # Top row
    for i in range(left, right + 1):
      matrix[top][i] = x
      x += 1
    top += 1
    
    # Right column
    for i in range(top, bottom + 1):
      matrix[i][right] = x
      x += 1
    right -= 1
    
    # Bottom row
    for i in range(right, left - 1, -1):
      matrix[bottom][i] = x
      x += 1
    bottom -= 1
    
    # Left column
    for i in range(bottom, top - 1, -1):
      matrix[i][left] = x
      x += 1
    left += 1
    
          
  return matrix