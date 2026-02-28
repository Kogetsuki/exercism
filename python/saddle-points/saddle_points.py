def saddle_points(matrix):
  if any(len(row) != len(matrix[0]) for row in matrix):
    raise ValueError("irregular matrix")
  
  max_row = [max(row) for row in matrix]
  min_col = [min(col) for col in zip(*matrix)]
    
  return [
    {"row": i + 1, "column": j + 1}
    for i, row in enumerate(matrix)
    for j, value in enumerate(row)
    if value == max_row[i] == min_col[j]
  ]
  
  