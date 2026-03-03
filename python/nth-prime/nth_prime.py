def prime_generator():
  primes = []
  candidate = 2

  while True:
    is_prime = True
    
    for prime in primes:
      if prime * prime > candidate:
        break
      
      if candidate % prime == 0:
        is_prime = False
        break
      
    if is_prime:
      primes.append(candidate)
      yield candidate
    
    candidate += 1
    
    
def prime(number):
  if number < 1:
    raise ValueError("there is no zeroth prime")
  
  primes = prime_generator()

  return [next(primes) for _ in range(number)][-1]