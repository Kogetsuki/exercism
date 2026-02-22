def egg_count(display_value):
  binary = str(bin(display_value)[2:])

  return sum(b == '1' for b in binary)
