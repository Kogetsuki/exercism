ANIMALS = [
  ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
  ("spider", "It wriggled and jiggled and tickled inside her."),
  ("bird", "How absurd to swallow a bird!"),
  ("cat", "Imagine that, to swallow a cat!"),
  ("dog", "What a hog, to swallow a dog!"),
  ("goat", "Just opened her throat and swallowed a goat!"),
  ("cow", "I don't know how she swallowed a cow!"),
  ("horse", "She's dead, of course!")
]

# Just one paragraph
def recite_verse(start_verse):
  result = []
  
  # First verse
  result.append(f"I know an old lady who swallowed a {ANIMALS[start_verse - 1][0]}.")

  # Animal-specific verse
  # Skip for the fly, it must be at the end
  if start_verse != 1:
    result.append(ANIMALS[start_verse - 1][1])

  # Dead if it is a horse
  if start_verse == 8:
    return result
  
  # Iterate through each animal
  while start_verse > 1:
    repetition_verse = f"She swallowed the {ANIMALS[start_verse - 1][0]} to catch the {ANIMALS[start_verse - 2][0]}"
    
    # Specific for the spider
    if start_verse == 3:
      repetition_verse += " that wriggled and jiggled and tickled inside her"

    result.append(repetition_verse + '.')
    start_verse -= 1
   
  # Add fly verse 
  result.append(ANIMALS[0][1])
  
  return result


def recite(start_verse, end_verse):
  result = []
  for i in range(start_verse, end_verse + 1):
    result.extend(recite_verse(i))
    result.append("")

  return result[:-1]
    


    