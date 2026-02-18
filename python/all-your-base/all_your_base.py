def to_base_10(input_base, digits):
  exposant = 0
  index = -1
  total = 0
  
  while exposant < len(digits):
    if digits[index] < 0 or digits[index] >= input_base:
      raise ValueError("all digits must satisfy 0 <= d < input base")
      
    total += digits[index] * input_base ** exposant
    index -= 1
    exposant += 1
  
  return total
  
  
def from_base_10(number, output_base):
  if number == 0:
    return [0]
  
  digits = []
  while number > 0:
    digits.append(number % output_base)
    number //= output_base
    
  return digits[::-1]


def rebase(input_base, digits, output_base):
  if input_base < 2:
    raise ValueError("input base must be >= 2")
  
  if output_base < 2:
    raise ValueError("output base must be >= 2")

  return from_base_10(to_base_10(input_base, digits), output_base)
