def is_vowel(c):
  return c.lower() in 'aeiou'


def translate_word(word):
  result = word

  if is_vowel(word[0]) or word.startswith('xr') or word.startswith('yt'):
    return result + 'ay'
  
  for i in range(len(word)):
    if word[i:i+2] == 'qu':
      return word[i+2:] + word[:i+2] + 'ay'
    
    if is_vowel(word[i]) or (word[i] == 'y' and i != 0):
      return word[i:] + word[:i] + 'ay'

  return word + 'ay'


def translate(text):
  return ' '.join(translate_word(w) for w in text.split())
  