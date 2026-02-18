import string

def is_pangram(sentence):
  histogram = [sentence.lower().count(c) for c in string.ascii_lowercase]
  return sorted(histogram)[0] > 0