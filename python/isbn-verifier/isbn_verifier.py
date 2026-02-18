def is_valid(isbn):
  isbn = isbn.replace('-', '').lower()

  if len(isbn) != 10:
    return False

  total = 0

  if isbn[-1].isdigit():
    total += int(isbn[-1])
  elif isbn[-1] == 'x':
    total += 10
  else:
    return False
  
  for i in range(len(isbn) - 1):
    if not isbn[i].isdigit():
      return False
    
    mult = 10 - i
    total += int(isbn[i]) * mult
  
    
  return total % 11 == 0