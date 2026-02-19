COLORS_LIST = [
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white"
]


METRIC_PREFIX = [
  "",
  "kilo",
  "mega",
  "giga",
  "tera"
]


def label(colors):
  result = ""
  duo = COLORS_LIST.index(colors[0]) * 10 + COLORS_LIST.index(colors[1])
  result += str(duo)

  third = COLORS_LIST.index(colors[2])
  while third > 0:
    result += "0"
    third -= 1
    
  prefix = 0
  while (int(result) // 1000) > 0:
    result = result[:-3]
    prefix += 1
  
  result += f" {METRIC_PREFIX[prefix]}ohms"
    
  return result
