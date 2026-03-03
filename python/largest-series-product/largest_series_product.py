import math

def get_product(serie):
  return math.prod(int(d) for d in serie)


def largest_product(series, size):
  if size > len(series):
    raise ValueError("span must not exceed string length")
  if size < 0:
    raise ValueError("span must not be negative")
  if any(not x.isdigit() for x in series):
    raise ValueError("digits input must only contain digits")
  
  possible_series = [
    series[i:i+size]
    for i in range(len(series) - size + 1)
  ]

  return max([get_product(s) for s in possible_series])
  