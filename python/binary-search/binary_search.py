def find_(search_list, value):
  if not search_list:
    raise ValueError("value not in array")
  
  mid = len(search_list) // 2
  
  if search_list[mid] == value:
    return search_list[mid]  

  return (
    (
      find_(search_list[:mid], value)
      if search_list[mid] > value
      else find_(search_list[mid+1:], value)
    )
  )


def find(search_list, value):
  return search_list.index(find_(search_list, value))


# print(find([1, 3, 4, 6, 8, 9, 11], 13))