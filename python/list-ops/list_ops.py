def append(list1, list2):
  result = [None] * (length(list1) + length(list2))
  
  for i, item in enumerate(list1):
    result[i] = item
  
  for i, item in enumerate(list2):
    result[length(list1) + i] = item

  return result
    
  
  
def concat(lists):
  result = []
  
  for list in lists:
    result = append(result, list)

  return result


def filter(function, list):
  result = []

  for item in list:
    if function(item):
      result = append(result, [item])

  return result


def length(list):
  count = 0
  for _ in list:
    count += 1
  
  return count


def map(function, list):
  result = []

  for item in list:
    result = append(result, [function(item)])

  return result


def foldl(function, list, initial):
  for item in list:
    initial = function(initial, item)

  return initial
  

def foldr(function, list, initial):
  for item in reverse(list):
    initial = function(initial, item)

  return initial


def reverse(list):
  return list[::-1]