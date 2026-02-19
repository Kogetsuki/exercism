import string


def translate(char):
  alphabet = string.ascii_lowercase
  complement = alphabet[::-1]

  return complement[alphabet.index(char)]


def encode(plain_text):
  result = ""
  count = 0
  
  for char in plain_text.lower():
    if char == " ":
      continue

    elif char.isalpha():
      result += translate(char)
      count += 1
      
    elif char.isdigit():
      result += char
      count += 1

    if count == 5:
      result += " "
      count = 0
      
  return result.strip()
    
  

def decode(ciphered_text):
  result = ""
  for char in ciphered_text:
    if char == " ":
      continue
    
    if char.isalpha():
      result += translate(char)

    else:
      result += char
  
  return result

print(encode("the quick brown fox jumps over the lazy dog"))