def rows(letter):
  index = ord(letter) - ord('A') + 1
  letter_to_print = 'A'
  
  width = index * 2 - 1
  height = width
  
  index -= 1
  
  rows_list = []
  
  for i in range(height // 2 + 1):
    to_print = ""

    for j in range(width):
      if j == index - i or j == index + i:
        to_print += letter_to_print
      else:
        to_print += ' '
        
    letter_to_print = chr(ord(letter_to_print) + 1)

    rows_list.append(to_print)
  
  return rows_list + rows_list[-2::-1]
    