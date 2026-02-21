from collections import Counter

def find_anagrams(word, candidates):
  result = []
  
  for candidate in candidates:
    if candidate.lower() == word.lower():
      continue
    
    if Counter(candidate.lower()) == Counter(word.lower()):
      result.append(candidate)

  return result
