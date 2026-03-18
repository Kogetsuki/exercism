def maximum_value(maximum_weight, items):
  maximum_values = [0] * (maximum_weight + 1)

  for item in items:
    weight = item['weight']
    value = item['value']

    for w in range(maximum_weight, weight - 1, -1):
      maximum_values[w] = max(maximum_values[w], value + maximum_values[w - weight])

  return maximum_values[maximum_weight]
