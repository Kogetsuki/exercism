def proverb(*words, qualifier):
  if not words:
    return []

  result = []
  for i in range(len(words) - 1):
    result.append(f"For want of a {words[i]} the {words[i+1]} was lost.")
    
  last_sentence = f"And all for the want of a"
  if qualifier:
    last_sentence += f" {qualifier}"
  last_sentence += f" {words[0]}."

  return [*result, last_sentence]