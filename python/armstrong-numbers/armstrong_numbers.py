def number_of_digits(number):
  result = 1
  while number // 10 > 0:
    result += 1
    number //= 10

  return result


def is_armstrong_number(number):
  if number < 0:
    raise ValueError("number must be a positive integer")
  
  digits_count = number_of_digits(number)
  n = number
  total = 0
  
  while n > 0:
    total += (n % 10) ** digits_count
    n //= 10
    
  return total == number