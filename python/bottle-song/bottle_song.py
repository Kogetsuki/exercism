NUMBERS = {
  0: "no",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten"
}


def recite(start, take=1):
  verses = []

  while take > 0:
    verse = [
      "",
      f"{NUMBERS[start].title()} green bottles hanging on the wall,",
      f"{NUMBERS[start].title()} green bottles hanging on the wall,",
      "And if one green bottle should accidentally fall,",
      f"There'll be {NUMBERS[start - 1]} green bottles hanging on the wall."
    ]
    
    if start == 2:
      verse[4] = verse[4].replace("bottles", "bottle")
      
    elif start == 1:
      for i in (1, 2):
        verse[i] = verse[i].replace("bottles", "bottle") 
     
    verses.extend(verse)
    start -= 1
    take -= 1
      
  return verses[1:]
