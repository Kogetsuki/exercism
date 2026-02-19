COLOR_LIST = [
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


def value(colors):
  return COLOR_LIST.index(colors[0]) * 10 + COLOR_LIST.index(colors[1])