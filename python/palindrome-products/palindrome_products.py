def is_palindrome(s):
  return s == s[::-1]


def get_palindrome_products(a, b):
  return {
    (i, j): i * j
    for i in range(a, b + 1)
    for j in range(i, b + 1)
    if is_palindrome(str(i * j))
  }


def largest(min_factor, max_factor):
  """Given a range of numbers, find the largest palindromes which
     are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
  """
  if min_factor > max_factor:
    raise ValueError("min must be <= max")

  palindrome_products = get_palindrome_products(min_factor, max_factor)
  if not palindrome_products:
    return (None, [])

  largest_product = max(palindrome_products.values())
  largest_factors = [
    k
    for k, v in palindrome_products.items()
    if v == largest_product
  ]

  return (largest_product, largest_factors)


def smallest(min_factor, max_factor):
  """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
  """
  if min_factor > max_factor:
    raise ValueError("min must be <= max")

  palindrome_products = get_palindrome_products(min_factor, max_factor)
  if not palindrome_products:
    return (None, [])

  smallest_product = min(palindrome_products.values())
  smallest_factors = [
    k
    for k, v in palindrome_products.items()
    if v == smallest_product
  ]

  return (smallest_product, smallest_factors)


print(largest(1, 9))
