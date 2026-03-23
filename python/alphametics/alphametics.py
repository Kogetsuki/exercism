import itertools

def solve(puzzle):
  # Split
  parts = puzzle.replace('+', ' ').replace('==', ' ').split()
  left_side = parts[:-1]
  right_side = parts[-1]

  # Unique letters
  letters = set("".join(parts))
  if len(letters) > 10:
    return None

  # Identify leading letters (cannot be 0)
  leading_letters = {
    word[0]
    for word in parts
    if len(word) > 1
  }

  # Compute weight of each letter
  # sum(weight * digit) == 0
  weights = {
    letter: 0
    for letter in letters
  }

  for word in left_side:
    for i, char in enumerate(reversed(word)):
      weights[char] += 10 ** i

  for i, char in enumerate(reversed(right_side)):
    weights[char] -= 10 ** i

  # Sort letters to keep leading at the front
  sorted_letters = sorted(
    weights.keys(),
    key=lambda l: l in leading_letters, reverse=True
  )

  sorted_weights = [
    weights[l]
    for l in sorted_letters
  ]

  # Indices of letters that cannot be zero
  leading_indices = [
    i
    for i, l in enumerate(sorted_letters)
    if l in leading_letters
  ]

  # Try all permutations of 0-9 for the number of unique letters
  for p in itertools.permutations(range(10), len(sorted_letters)):
    # Check leading zero constraint
    if any(p[i] == 0 for i in leading_indices):
      continue

    # Check if weighted sum equals zero
    if sum(w * d for w, d in zip(sorted_weights, p)) == 0:
      return dict(zip(sorted_letters, p))

  return None
