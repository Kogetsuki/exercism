from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "two"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four of a kind"
LITTLE_STRAIGHT = "little straight"
BIG_STRAIGHT = "big straight"
CHOICE = "choice"


NUMBER_CATEGORIES = {
  ONES: 1,
  TWOS: 2,
  THREES: 3,
  FOURS: 4,
  FIVES: 5,
  SIXES: 6,
}


def score(dice, category):
  # Count occurrences
  counts = Counter(dice)
  # Total value
  total = sum(dice)
  
  # ONES through SIXES
  if category in NUMBER_CATEGORIES:
    value = NUMBER_CATEGORIES[category]
    return counts[value] * value
  
  # val1 * 2 and val2 * 3
  if category == FULL_HOUSE:
    return (
      total
      if sorted(counts.values()) == [2, 3]
      else 0
    )
    
  if category == FOUR_OF_A_KIND:
    for value, count in counts.items():
      if count >= 4:
        return value * 4
    return 0
    
  # 1-2-3-4-5
  if category == LITTLE_STRAIGHT:
    return (
      30
      if set(dice) == {1, 2, 3, 4, 5}
      else 0
    )
    
  # 2-3-4-5-6
  if category == BIG_STRAIGHT:
    return (
      30
      if set(dice) == {2, 3, 4, 5, 6}
      else 0
    )
  
  # Sum of the dices
  if category == CHOICE:
    return total
  
  # All dice same value
  if category == YACHT:
    return (
      50
      if len(counts) == 1
      else 0
    )
    
  return 0
  