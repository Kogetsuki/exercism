def square_of_sum(number):
  nums = list(range(1, number + 1))
  return sum(nums) ** 2
  

def sum_of_squares(number):
  nums = [i * i for i in range(1, number + 1)]
  return sum(nums)


def difference_of_squares(number):
  return square_of_sum(number) - sum_of_squares(number)