import itertools

def combinations(target, size, exclude):
  series = [
    i
    for i in range(1, 10)
    if i not in exclude
  ]

  return [
    list(combo)
    for combo in list(itertools.combinations(series, size))
    if sum(combo) == target
  ]
