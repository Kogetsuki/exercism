def rectangles(strings):
  if not strings:
    return 0
  
  height = len(strings)
  width = len(strings[0])
  count = 0
  
  for top in range(height):
    for bottom in range(top + 1, height):
      cols = [
        c for c in range(width)
        if strings[top][c] == '+' and strings[bottom][c] == '+'
      ]
      
      for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
          left, right = cols[i], cols[j]
          
          if (
            all(
              strings[top][c] in "-+" and strings[bottom][c] in "-+"
              for c in range(left + 1, right)
            )
            and
            all(
              strings[r][left] in "|+" and strings[r][right] in "|+"
              for r in range(top + 1, bottom)
            )
          ):
            count += 1
            
  return count