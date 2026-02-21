def check_case(garden, i, j):
  height = len(garden)
  width = len(garden[0])

  flower_count = sum(
    garden[i + di][j + dj] == '*'
    for di in (-1, 0, 1)
    for dj in (-1, 0, 1)
    if not (di == 0 and dj == 0)
    if 0 <= i + di < height
    if 0 <= j + dj < width
  )

  if flower_count == 0:
    return ' '
  
  return str(flower_count)


def annotate(garden):
  if not garden:
    return []
  
  height = len(garden)
  width = len(garden[0])
  
  if any(len(row) != width for row in garden):
    raise ValueError("The board is invalid with current input.")
  
  result = []
  
  for i in range(height):
    row = ""

    for j in range(width):
      if garden[i][j] == '*':
        row += '*'
      elif garden[i][j] == ' ':
        row += check_case(garden, i, j)
      else:
        raise ValueError("The board is invalid with current input.")
        
    result.append(row)
    
  return result