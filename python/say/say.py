LITERALS = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
}


POWERS = ["", "thousand", "million", "billion"]


# Takes number of 3 digits or less
# and a power representing where we are on the whole number
def get_literal(n, power):
  if n == 0:
    return ""
    
  res = ""

  if n // 100 != 0:
    res += f"{LITERALS[n // 100]} hundred"
    n %= 100
    
  if n == 0:
    return res
    
  if n < 20:
    res += LITERALS[n]
  
  else:  
    unity = n % 10
    n -= unity
    
    if n == 0:
      res += f" {LITERALS[unity]}"
    
    elif unity == 0:
      res += f" {LITERALS[n]}"

    else:
      res += f" {LITERALS[n]}-{LITERALS[unity]}"

  return f"{res} {POWERS[power]} "


def say(number):
  if number < 0 or number > 999_999_999_999:
    raise ValueError("input out of range")

  if number == 0:
    return "zero"
  
  packs = []

  while number > 0:
    packs.append(number % 1000)
    number //= 1000
    
  print(packs)
  
  result = ""
  for i, pack in enumerate(packs):
    result = get_literal(pack, i) + result

  return result.strip()
  
print(say(170))