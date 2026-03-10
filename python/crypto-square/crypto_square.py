import re
import math

# Remove punctuation, spaces and lower
def normalize_text(plain_text):
  return re.sub(r"[^A-Za-z0-9]", "", plain_text).lower()


# Compute the size of the rectangle
# Based on the length of the normalized text
def get_rectangle_size(length):
  r = int(math.sqrt(length))
  c = math.ceil(math.sqrt(length))
  
  if r * c < length:
    r += 1

  return r, c


# Square the text given the computed size
def get_square(text, col):
  return [
    text[i:i+col].ljust(col)
    for i in range(0, len(text), col)
  ]


# Get the resulted ciphered text
def cipher_text(plain_text):
  text = normalize_text(plain_text)
  if not text:
    return ""

  _, columns = get_rectangle_size(len(text))
  square = get_square(text, columns)
  
  return ' '.join(
    ''.join(col)
    for col in zip(*square)
  )
