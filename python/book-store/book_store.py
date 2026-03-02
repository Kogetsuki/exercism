from functools import lru_cache
from collections import Counter

PRICE = 8

DISCOUNT = {
  1: 0.00,
  2: 0.05,
  3: 0.10,
  4: 0.20,
  5: 0.25
}



def total(basket):
  if not basket:
    return 0
  
  counts = tuple(sorted(Counter(basket).values(), reverse=True))

  @lru_cache(None)
  def min_price(state):
    if not state:
      return 0
    
    best = float('inf')
    
    distinct = len(state)

    for k in range(1, distinct + 1):
      new_state = list(state)
      for i in range(k):
        new_state[i] -= 1

      new_state = tuple(sorted((c for c in new_state if c > 0), reverse=True))
      group_cost = int(k * PRICE * (1 - DISCOUNT[k]) * 100)
      cost = group_cost + min_price(new_state)

      best = min(best, cost)
      
    return best
  
  return min_price(counts)
  
total([1, 1, 2, 2, 3, 3, 4, 5])