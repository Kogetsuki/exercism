import operator

def answer(question):
  if not question.startswith("What is ") or not question.endswith("?"):
      raise ValueError("syntax error")

  # Remove questioning
  expression = question[8:-1].strip()
  if not expression:
    raise ValueError("syntax error")

  # Supported operations mapping
  ops = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied by": operator.mul,
    "divided by": operator.floordiv
  }

  # Tokenize
  tokens = []
  i = 0
  words = expression.split()
  while i < len(words):
    word = words[i]
    if word.lstrip('-').isdigit(): 
      tokens.append(int(word))
      i += 1

    else:
      # Check for two-word operations
      if i + 1 < len(words):
        two_word_op = f"{words[i]} {words[i+1]}"
        if two_word_op in ops:
          tokens.append(two_word_op)
          i += 2
          continue
        
      # Check for one-word operations
      if word in ops:
        tokens.append(word)
        i += 1

      else:
        raise ValueError("unknown operation")

  # Evaluate left-to-right
  if len(tokens) < 1 or not isinstance(tokens[0], int):
      raise ValueError("syntax error")

  result = tokens[0]
  i = 1
  while i < len(tokens):
    if i + 1 >= len(tokens):
      raise ValueError("syntax error")

    op_token = tokens[i]
    num = tokens[i + 1]
    if not isinstance(num, int):
      raise ValueError("syntax error")
      
    if op_token not in ops:
      raise ValueError("unknown operation")

    result = ops[op_token](result, num)
    i += 2

  return result
