import random
import string


class Cipher:
  def __init__(self, key=None):
    if key:
      self.key = key
    else:
      self.key = self._generate_random_key()


  def _generate_random_key(self):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
  
  
  def _shift(self, text, direction):
    result = []

    for i, c in enumerate(text):
      k = self.key[i % len(self.key)]
      shift = ord(k) - ord('a')
      
      if direction == -1:
        shift = -shift
        
      result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
      
    return ''.join(result)


  def encode(self, text):
    return self._shift(text, 1)
    

  def decode(self, text):
    return self._shift(text, -1)
  
  
print(Cipher("iamapandabear").encode("iamapandabear"))