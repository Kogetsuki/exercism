# Custom error class
class StackUnderflowError(Exception):
  def __init__(self, message):
    self.message = message

# ===================================================================== 
# Helper
# ===================================================================== 
def is_number(token):
  return token.lstrip("-").isdigit()


def require_stack_size(stack, size):
  if len(stack) < size:
    raise StackUnderflowError("Insufficient number of items in stack")

    
# ===================================================================== 
# Stack Operations
# ===================================================================== 
def op_dup(stack):
  require_stack_size(stack, 1)
  stack.append(stack[-1])

  
def op_drop(stack):
  require_stack_size(stack, 1)
  stack.pop()
  

def op_swap(stack):
  require_stack_size(stack, 2)
  stack[-1], stack[-2] = stack[-2], stack[-1]
  
  
def op_over(stack):
  require_stack_size(stack, 2)
  stack.append(stack[-2])
  
  
# ===================================================================== 
# Arithmetic Operations
# ===================================================================== 
def op_add(stack):
  require_stack_size(stack, 2)
  b = stack.pop()
  a = stack.pop()
  stack.append(a + b)

  
def op_sub(stack):
  require_stack_size(stack, 2)
  b = stack.pop()
  a = stack.pop()
  stack.append(a - b)
  
  
def op_mul(stack):
  require_stack_size(stack, 2)
  b = stack.pop()
  a = stack.pop()
  stack.append(a * b)
  
  
def op_div(stack):
  require_stack_size(stack, 2)
  b = stack.pop()
  if b == 0:
    raise ZeroDivisionError("divide by zero")
  a = stack.pop()
  stack.append(a // b)
  

# ===================================================================== 
# Token association
# ===================================================================== 
BUILTINS = {
  "+": op_add,
  "-": op_sub,
  "*": op_mul,
  "/": op_div,
  "dup": op_dup,
  "drop": op_drop,
  "swap": op_swap,
  "over": op_over
}


# ===================================================================== 
# Word definition
# ===================================================================== 
def parse_definitions(tokens, definitions):
  if len(tokens) < 3:
    raise ValueError("invalid definition")
  
  name = tokens[1]

  if is_number(name):
    raise ValueError("illegal operation")
  
  try:
    end = tokens.index(";")
  except ValueError:
    raise ValueError("invalid definition")

  raw_body = tokens[2:end]
  if not raw_body:
    raise ValueError("invalid definition")
  
  compiled_body = []
  for token in raw_body:
    if token in definitions:
      compiled_body.extend(definitions[token])
    else:
      compiled_body.append(token)
  
  definitions[name] = compiled_body
  
  return tokens[end + 1:]


def expand_token(token, definitions):
  if token in definitions:
    return definitions[token]
  
  return [token]


# ===================================================================== 
# Evaluator
# ===================================================================== 
def evaluate(input_data):
  stack = []
  definitions = {}

  for line in input_data:
    tokens = line.lower().split()

    while tokens:
      token = tokens.pop(0)
      
      if token == ":":
        tokens = parse_definitions([":"] + tokens, definitions)
        continue
        
      for sub_token in expand_token(token, definitions):
        if is_number(sub_token):
          stack.append(int(sub_token))
        elif sub_token in BUILTINS:
          BUILTINS[sub_token](stack)
        else:
          raise ValueError("undefined operation")
    
  return stack