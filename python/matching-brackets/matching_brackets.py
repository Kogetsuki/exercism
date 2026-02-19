def is_paired(input_string):
  stack = []
  pairs = {')': '(', ']': '[', '}': '{'}

  for c in input_string:
    if c in '([{':
      stack.append(c)

    elif c in ')]}':
      if not stack or stack[-1] != pairs[c]:
        return False
      stack.pop()

  return not stack
