def decode(string):
  result = ""
  i = 0

  while i < len(string):
    char = ""
    count = ""

    while True:
      if not string[i].isdigit():
        char = string[i]
        break
      
      count += string[i]
      i += 1
      
    if not count:
      count = 1
      
    result += char * int(count)
    i += 1

  print(result)
  return result


def encode(string):
  result = ""
  i = 0

  while i < len(string):
    char = string[i]
    count = 0
    
    while True:
      if i >= len(string) or string[i] != char:
        break
      
      i += 1
      count += 1

    if count == 1:
      result += char
    else:
      result += f"{count}{char}"

  return result
