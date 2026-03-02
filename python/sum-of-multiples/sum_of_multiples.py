def get_multiples(limit, base):
  if base == 0 or base > limit:
    return {}
  return {x for x in range(base, limit, base)}
  

def sum_of_multiples(limit, multiples):
  return sum({
    x
    for base in multiples
    for x in get_multiples(limit, base)
  })
  