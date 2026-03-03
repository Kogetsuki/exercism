import random

class Character:
  def __init__(self):
    # Init abilities
    self.strength = self.ability()
    self.dexterity = self.ability()
    self.constitution = self.ability()
    self.intelligence = self.ability()
    self.wisdom = self.ability()
    self.charisma = self.ability()
    
    # Init hitpoints depending on constitution
    self.hitpoints = 10 + modifier(self.constitution)


  # Roll 6-sided dice
  def roll_dice(self):
    return random.randint(1, 6)
  
  
  # Calculate ability score
  # Roll 4 6-sided dices, keep 3 largest
  def ability(self):
    scores = [self.roll_dice() for _ in range(4)]
    scores.remove(min(scores))
    
    return sum(scores)
    

def modifier(value):
  return (value - 10) // 2
  