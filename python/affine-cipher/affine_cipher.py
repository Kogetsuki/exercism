from itertools import batched
import re
from math import gcd


def encode(plain_text, a, b):
  # Check co prime
  if not is_co_prime(a, 26):
    raise ValueError("a and m must be coprime.")

  # Remove spaces, punctuations and change to lowercase
  plain_text = re.sub(r"[^\w]", "", plain_text).lower()
  result = []

  for c in plain_text:
    # If digit, keep it not encoded
    if c.isdigit():
      result.append(c)
      continue

    # Encode
    encoded = (a * get_numeric(c) + b) % 26
    result.append(get_letter(encoded))

  # Get by packs of 5
  return ' '.join(''.join(batch) for batch in batched(result, 5))


def decode(ciphered_text, a, b):
  # Check co prime
  if not is_co_prime(a, 26):
    raise ValueError("a and m must be coprime.")

  x = get_MMI(a)

  result = []

  for c in ciphered_text:
    # Skip spaces
    if c == " ":
      continue

    if c.isdigit():
      result.append(c)
      continue

    decoded = (x * (get_numeric(c) - b)) % 26
    result.append(get_letter(decoded))

  return ''.join(result)

# =====================================================================
# HELPERS
# =====================================================================
# Compute numerical value of a letter from 0 to 25
def get_numeric(letter):
  return ord(letter) - ord('a')


# Convert a numerical value from 0 to 25 to its letter equivalent
def get_letter(numeric):
  return chr(numeric + ord('a'))


def is_co_prime(a, b):
  return gcd(a, b) == 1


# Compute Modular Multiplicative Inverse of a positive integer
def get_MMI(a):
  for x in range(25, 0, -1):
    if (a * x) % 26 == 1:
      return x
