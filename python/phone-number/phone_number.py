import re

class PhoneNumber:
  def __init__(self, number):
    # Check for letters
    if re.search(r"[a-zA-Z]", number):
      raise ValueError("letters not permitted")
    
    # Check for punctuations
    if re.search(r"[^\d\s().+-]", number):
      raise ValueError("punctuations not permitted")

    # Keep only digits
    cleaned = re.sub(r"[\D]", "", number)
  
    # Check when country code is present
    if len(cleaned) == 11:
      if cleaned[0] != '1':
        raise ValueError("11 digits must start with 1")
      cleaned = cleaned[1:]
    elif len(cleaned) < 10:
      raise ValueError("must not be fewer than 10 digits")
    elif len(cleaned) > 11:
      raise ValueError("must not be greater than 11 digits")
    elif len(cleaned) == 10:
      pass
    
    # Check area code
    if cleaned[0] == '0':
      raise ValueError("area code cannot start with zero")
    if cleaned[0] == '1':
      raise ValueError("area code cannot start with one")

    # Chek exchange code
    if cleaned[3] == '0':
      raise ValueError("exchange code cannot start with zero")
    if cleaned[3] == '1':
      raise ValueError("exchange code cannot start with one")
    
    self.number = cleaned
    self.area_code = cleaned[:3]
    self.exchange_code = cleaned[3:6]
    self.subscriber_code = cleaned[6:]
    
    
  def pretty(self):
    return f"({self.area_code})-{self.exchange_code}-{self.subscriber_code}"

