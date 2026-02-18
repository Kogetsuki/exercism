def rotate(text, key):
  result = []
  
  for c in text:
    if c.islower():
      result.append(chr((ord(c) - ord('a') + key) % 26 + ord('a')))
    elif c.isupper():
      result.append(chr((ord(c) - ord('A') + key) % 26 + ord('A')))
    else:
      result.append(c)
    
  return ''.join(result)
