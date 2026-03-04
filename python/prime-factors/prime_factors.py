def factors(value):
  result = []
  
  candidate = 2
  
  while candidate <= value:
    if value % candidate == 0:
      result.append(candidate)
      value //= candidate
    
    else:
      candidate += 1

  return result

