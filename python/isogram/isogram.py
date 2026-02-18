from collections import Counter

def is_isogram(string):
  letter_counts = Counter(c.lower() for c in string if c.isalpha())
  return len(letter_counts) == 0 or letter_counts.most_common(1)[0][1] == 1
