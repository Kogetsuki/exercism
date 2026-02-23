gifts = [
  ("first", "a Partridge in a Pear Tree"),
  ("second", "two Turtle Doves"),
  ("third", "three French Hens"),
  ("fourth", "four Calling Birds"),
  ("fifth", "five Gold Rings"),
  ("sixth", "six Geese-a-Laying"),
  ("seventh", "seven Swans-a-Swimming"),
  ("eighth", "eight Maids-a-Milking"),
  ("ninth", "nine Ladies Dancing"),
  ("tenth", "ten Lords-a-Leaping"),
  ("eleventh", "eleven Pipers Piping"),
  ("twelfth", "twelve Drummers Drumming")
]


def recite(start_verse, end_verse):
  verses = []
  
  for i in range(start_verse, end_verse + 1):
    day = gifts[i - 1][0]
    verse = f"On the {day} day of Christmas my true love gave to me: "

    for j in range(i, 1, -1):
      verse += f"{gifts[j - 1][1]}, "
      
    if day != 'first':
      verse += f"and {gifts[0][1]}."
    else:
      verse += f"{gifts[0][1]}."
    
    verses.append(verse)  
  
  return verses