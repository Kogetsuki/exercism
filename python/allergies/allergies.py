class Allergies:
  ALLERGIES = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128
  }
  
  
  def __init__(self, score):
    self.score, self.power = self.adjust_score(score)
    self.allergies = []
    self.init_allergies()
    
  
  # Compute the greatest power of 2 smaller than score
  def adjust_score(self, score):
    largest_power = 1 << (score.bit_length() - 1) if score else 0
    if largest_power >= 256:
      score -= largest_power

    return score, largest_power
  
  
  def init_allergies(self):
    score = self.score
    
    for key, value in reversed(self.ALLERGIES.items()):
      if score >= value:
        score -= value
        self.allergies.append(key)


  def allergic_to(self, item):
    return item in self.allergies
    

  @property
  def lst(self):
    return self.allergies
