def check_pythagore_and_sum(a, b, c):
  return a*a + b*b == c*c


def triplets_with_sum(number):
  triplets = []

  for a in range(1, number // 3):
    for b in range(a + 1, number // 2):
      c = number - a - b   

      if check_pythagore_and_sum(a, b, c):
        triplets.append([a, b, c])

  return triplets

print(triplets_with_sum(12))