def convert(number):
  result = (
    ("Pling" if number % 3 == 0 else "") +
    ("Plang" if number % 5 == 0 else "") +
    ("Plong" if number % 7 == 0 else "")
  )
  
  return result or str(number)