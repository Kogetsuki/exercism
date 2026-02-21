TASKS = {
  -1: "wink",
  -2: "double blink",
  -3: "close your eyes",
  -4: "jump"
}


def commands(binary_str):
  result = []

  for i in range(-1, -5, -1):
    if binary_str[i] == '1':
      result.append(TASKS[i])

  if binary_str[0] == '1':
    return result[::-1]

  return result
