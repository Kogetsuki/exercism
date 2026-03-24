from collections import deque
from math import gcd

def measure(bucket_one, bucket_two, goal, start_bucket):
  # Validate input
  if goal > max(bucket_one, bucket_two):
    raise ValueError("Goal is larger than both buckets.")
  if goal % gcd(bucket_one, bucket_two) != 0:
    raise ValueError("Goal cannot be measured with these bucket sizes.")

  # Initial state depending on starting bucket
  if start_bucket == "one":
    start_state = (bucket_one, 0, 1)
  elif start_bucket == "two":
    start_state = (0, bucket_two, 1)
  else:
    raise ValueError("Invalid starting bucket name.")

  queue = deque([start_state])
  visited = set([(start_state[0], start_state[1])])

  while queue:
    a, b, actions = queue.popleft()

    # Check if goal is reached
    if a == goal:
      return (actions, "one", b)
    if b == goal:
      return (actions, "two", a)

    # Generate all possible next moves
    next_states = []

    # Fill bucket one
    if a != bucket_one:
      next_states.append((bucket_one, b, actions + 1))

    # Fill bucket two
    if b != bucket_two:
      next_states.append((a, bucket_two, actions + 1))

    # Empty bucket one
    if a != 0:
      next_states.append((0, b, actions + 1))

    # Empty bucket two
    if b != 0:
      next_states.append((a, 0, actions + 1))

    # Pour bucket one -> bucket two
    pour = min(a, bucket_two - b)
    if pour > 0:
      next_states.append((a - pour, b + pour, actions + 1))

    # Pour bucket two -> bucket one
    pour = min(b, bucket_one - a)
    if pour > 0:
      next_states.append((a + pour, b - pour, actions + 1))

    for state in next_states:
      sa, sb, _ = state

      # Forbidden state: starting bucket empty and other full
      if start_bucket == "one" and sa == 0 and sb == bucket_two:
        continue
      if start_bucket == "two" and sb == 0 and sa == bucket_one:
        continue

      if (sa, sb) not in visited:
        visited.add((sa, sb))
        queue.append(state)

  # If BFS finishes without finding goal
  raise ValueError("It is not possible to reach the goal with these buckets.")
