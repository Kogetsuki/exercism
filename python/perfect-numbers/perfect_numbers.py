def aliquot(number):
  multiples = [1]
  i = 2
  while i < number ** 0.5:
    if number % i == 0:
      multiples += [i, number // i]
    
    i += 1
    
  return multiples
  


def classify(number):
  """ A perfect number equals the sum of its positive divisors.

  :param number: int a positive integer
  :return: str the classification of the input integer
  """
  if number < 1:
    raise ValueError("Classification is only possible for positive integers.")
  
  if number == 1:
    return 'deficient'

  aliquot_sum = sum(aliquot(number))

  if number == aliquot_sum:
    return 'perfect'
  if number < aliquot_sum:
    return 'abundant'
  return 'deficient'