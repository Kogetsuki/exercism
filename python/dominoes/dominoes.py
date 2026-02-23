# Flip domino: Invert the tuple
# e.g (3,2) => (2,3)
def flip_domino(d):
  return d[::-1]


# Check if two dominoes can be chained together
def is_domino_chainable(d1, d2):
  return d1[1] == d2[0]


# Checks validity of a chain 
def is_valid_chain(chain):
  return (
    # Chain exists
    chain and
    # First and last stone match
    chain[0][0] == chain[-1][1] and
    # All consecutive stones match
    all(chain[i][1] == chain[i+1][0] for i in range(len(chain) - 1))
  )


# Recursive backtracking to build chain
def can_chain_rec(chain, dominoes, marked):
  # All dominoes are used
  if len(chain) == len(dominoes):
    return (
      # Success
      chain
      if is_valid_chain(chain)
      # Failure
      else None
    )
  
  # Get last domino
  last = chain[-1]

  # Try every domino that hasnt been used
  for i, d in enumerate(dominoes):
    if marked[i]:
      continue
    
    # Try both orientations
    for candidate in [d, flip_domino(d)]:
      if not is_domino_chainable(last, candidate):
        continue
      
      # Add to chain and marked as used
      chain.append(candidate)
      marked[i] = True

      # Attempt to execute the chain
      result = can_chain_rec(chain, dominoes, marked)
      if result:
        return result
      
      # Backtrack
      chain.pop()
      marked[i] = False
      
  # No valid chain in this branch
  return None
  


def can_chain(dominoes):
  if not dominoes:
    return []
  
  # Try each domino as starting point
  for i, first in enumerate(dominoes):
    for candidate in [first, flip_domino(first)]:
      chain = [candidate]
      marked = [False] * len(dominoes)
      marked[i] = True

      # Start recursive bactracking
      result = can_chain_rec(chain, dominoes, marked)
      if result:
        return result
      
  # No valid chain
  return None
