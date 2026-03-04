import re

def abbreviate(words):
  word_list = re.split(r"[ _-]+", words)
  
  return ''.join(
    w[0].upper()
    for w in word_list
  )
