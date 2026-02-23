def find_fewest_coins(coins, target):
  if target < 0:
    raise ValueError("target can't be negative")
  
  min_coins = [float('inf')] * (target + 1) # Superior to max_value possible
  min_coins[0] = 0
  
  for i in range(1, target + 1):
    min_coins[i] = min(
      (min_coins[i - coin] + 1 for coin in coins if i >= coin),
      default=float('inf')  
    )
    
  if min_coins[target] == float('inf'):
    raise ValueError("can't make target with given coins")
  
  result = []
  
  for coin in coins:
    while target > 0:
      if target >= coin and min_coins[target] == min_coins[target - coin] + 1:
        result.append(coin)
        target -= coin
      
      else:
        break
        
  return result
        