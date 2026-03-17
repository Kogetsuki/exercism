# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
  def __init__(self, word):
    self.word = word
    self.remaining_guesses = 9
    self.status = STATUS_ONGOING
    self.ongoing = ['_'] * len(word)
    self.guesses = set()


  def guess(self, char):
    # Game ended
    if self.status != STATUS_ONGOING:
      raise ValueError("The game has already ended.")

    # Failure
    if char in self.guesses or char not in self.word:
      self.remaining_guesses -= 1

    # Mark guessed chars
    self.guesses.add(char)

    # Detect correct letters
    for i, c in enumerate(self.word):
      if c == char:
        self.ongoing[i] = c


    # End game
    if '_' not in self.ongoing:
      self.status = STATUS_WIN
    if self.remaining_guesses < 0:
      self.status = STATUS_LOSE


  def get_masked_word(self):
    return ''.join(self.ongoing)


  def get_status(self):
    return self.status
