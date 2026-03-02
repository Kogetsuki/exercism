def get_multiples(limit, base):
  return [x for x in range(base * 2, limit + 1, base)]


def primes(limit):
  numbers = [x for x in range(2, limit + 1)]
  marks = [0] * len(numbers)

  for i, n in enumerate(numbers):
    if marks[i]:
      continue

    for mult in get_multiples(limit, n):
      marks[mult - 2] = 1
  
  return [x for i, x in enumerate(numbers) if not marks[i]]
  
print(primes(10))