ASCII_DIGITS = {
  "0": [" _ ", "| |", "|_|"],
  "1": ["   ", "  |", "  |"],
  "2": [" _ ", " _|", "|_ "],
  "3": [" _ ", " _|", " _|"],
  "4": ["   ", "|_|", "  |"],
  "5": [" _ ", "|_ ", " _|"],
  "6": [" _ ", "|_ ", "|_|"],
  "7": [" _ ", "  |", "  |"],
  "8": [" _ ", "|_|", "|_|"],
  "9": [" _ ", "|_|", " _|"],
}


# Reverse lookup dict method
def reverse_lookup(list):
  for k, v in ASCII_DIGITS.items():
    if v == list:
      return k
  return "?"
  

def convert(input_grid):
  if len(input_grid) % 4 != 0:
    raise ValueError("Number of input lines is not a multiple of four")

  if any(len(input_grid[i]) % 3 != 0 for i in range(len(input_grid))):
    raise ValueError("Number of input columns is not a multiple of three")

  result = ""
  for x in range(0, len(input_grid), 4):
    for i in range(0, len(input_grid[x]), 3):
      digit = [input_grid[j][i:i+3] for j in range(x, x + 3)]
      result += reverse_lookup(digit)
    result += ","
    
  return result[:-1]
    