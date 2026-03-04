SCORE_LETTERS = {
  1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
  2: ["D", "G"],
  3: ["B", "C", "M", "P"],
  4: ["F", "H", "V", "W", "Y"],
  5: ["K"],
  8: ["J", "X"],
  10: ["Q", "Z"]
}


LETTER_SCORES = {
  letter: score
  for score, letters in SCORE_LETTERS.items()
  for letter in letters
}


def score(word):
  return sum(
    LETTER_SCORES[letter]
    for letter in word.upper()
  )

