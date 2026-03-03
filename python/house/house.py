PARTS = [
    ("the house that Jack built.", ""),
    ("the malt", "that lay in "),
    ("the rat", "that ate "),
    ("the cat", "that killed "),
    ("the dog", "that worried "),
    ("the cow with the crumpled horn", "that tossed "),
    ("the maiden all forlorn", "that milked "),
    ("the man all tattered and torn", "that kissed "),
    ("the priest all shaven and shorn", "that married "),
    ("the rooster that crowed in the morn", "that woke "),
    ("the farmer sowing his corn", "that kept "),
    ("the horse and the hound and the horn", "that belonged to "),
]


def recite(start_verse, end_verse):
  verses = []

  for verse_number in range(start_verse - 1, end_verse):
    lines = [f"This is {PARTS[verse_number][0]}"]

    for i in range(verse_number, 0, -1):
      noun, verb = PARTS[i]
      prev_noun, _ = PARTS[i - 1]

      lines.append(verb + prev_noun)

    verses.append(" ".join(lines))

  return verses