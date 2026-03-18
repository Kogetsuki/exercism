class BowlingGame:
  def __init__(self):
    self.rolls = []


  def roll(self, pins):
    if not 0 <= pins <= 10:
      raise ValueError("pins must be between 0 and 10")

    if self.is_game_complete():
      raise ValueError("cannot roll after game finished")

    # Invalid frame totals
    if self.is_second_roll_of_frame() and self.rolls[-1] + pins > 10:
      raise ValueError("two rolls in a frame cannot score more than 10 points")

    # 10th frame bonus
    if self.is_in_tenth_frame_bonus():
      last_roll = self.rolls[-1]
      if last_roll < 10 and last_roll + pins > 10:
        raise ValueError("two rolls in a frame cannot score more than 10 points")

    self.rolls.append(pins)


  def score(self):
    if not self.is_game_complete():
      raise ValueError("incomplete game cannot be scored")

    total = 0
    roll_index = 0

    for _ in range(10):
      if self.is_strike(roll_index):
        total += 10 + self.strike_bonus(roll_index)
        roll_index += 1
      elif self.is_spare(roll_index):
        total += 10 + self.spare_bonus(roll_index)
        roll_index += 2
      else:
        total += self.frame_total(roll_index)
        roll_index += 2

    return total


  # =====================================================================
  # HELPER
  # =====================================================================
  def is_strike(self, i):
    return self.rolls[i] == 10


  def is_spare(self, i):
    return self.rolls[i] + self.rolls[i+1] == 10


  def strike_bonus(self, i):
    return self.rolls[i+1] + self.rolls[i+2]


  def spare_bonus(self, i):
    return self.rolls[i+2]


  def frame_total(self, i):
    return self.rolls[i] + self.rolls[i+1]


  def is_game_complete(self):
    try:
      r_index = 0
      for f in range(10):
        if self.rolls[r_index] == 10:
          r_index += 1
        else:
          r_index += 2

      tenth_start = r_index - (1 if self.rolls[r_index-1] == 10 else 2)

      if self.is_strike(tenth_start) or self.is_spare(tenth_start):
        return len(self.rolls) == tenth_start + 3
      return len(self.rolls) == tenth_start + 2

    except IndexError:
      return False


  def is_second_roll_of_frame(self):
    r_idx = 0

    for f in range(9):  # Only check first 9 frames
      if r_idx == len(self.rolls):
        return False

      if self.rolls[r_idx] == 10:
        r_idx += 1
      else:
        r_idx += 1

        if r_idx == len(self.rolls):
          return True

        r_idx += 1

    return False


  def is_in_tenth_frame_bonus(self):
    # Specific check for the 10th frame fill balls
    r_idx = 0

    for f in range(9):
      if r_idx >= len(self.rolls):
        return False

      r_idx += 1 if self.rolls[r_idx] == 10 else 2

    # We are in the 10th frame area
    tenth_rolls = self.rolls[r_idx:]

    if len(tenth_rolls) == 2 and tenth_rolls[0] == 10 and tenth_rolls[1] < 10:
      return True

    return False
