class Luhn:
  def __init__(self, card_num):
    # Remove spaces
    self.card_num = card_num.replace(" ", "")


  def valid(self):
    # Input must be of len > 1
    # All chars must be spaces or digits
    if len(self.card_num) < 2 or any(not x.isdigit() for x in self.card_num):
      return False
    
    # Convert to list[int] for mutable
    num = [int(d) for d in self.card_num]
    # Start from the end
    i = len(num) - 2
    
    while i >= 0:
      # Double
      # Max is 9
      num[i] *= 2
      if num[i] > 9:
        num[i] -= 9
        
      # Only odd index
      i -= 2
      
    # Sum all digits
    total = sum(num)

    # Check evenly divisible by 10
    return (10 - (total % 10)) % 10 == 0
  