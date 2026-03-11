def handle_step(step, k, rails):
  if k == 0:
    return 1
  elif k == rails - 1:
    return -1
  return step


def encode(message, rails):
  rails_list = [
    []
    for _ in range(rails)
  ]

  k = 0
  step = 1

  for c in message:
    rails_list[k].append(c)

    step = handle_step(step, k, rails)
    k += step

  return ''.join(
    ''.join(r)
    for r in rails_list
  )



def decode(encoded_message, rails):
  n = len(encoded_message)
  rails_list = [
    [
      ''
      for _ in range(n)
    ]
    for _ in range(rails)
  ]

  k = 0
  step = 1

  # Mark zig-zag pos
  for i in range(n):
    rails_list[k][i] = '?'

    step = handle_step(step, k, rails)
    k += step

  # Fill with char
  idx = 0
  for r in range(rails):
    for c in range(n):
      if rails_list[r][c] == '?':
        rails_list[r][c] = encoded_message[idx]
        idx += 1

  # Read to reconstruct message
  result = []
  k = 0
  step = 1

  for i in range(n):
    result.append(rails_list[k][i])

    step = handle_step(step, k, rails)
    k += step

  return ''.join(result)
