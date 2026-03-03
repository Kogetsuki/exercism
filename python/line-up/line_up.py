def get_ending(number):
  nb_string = str(number)
  
  if nb_string[-1] == "1" and nb_string[-2:] != "11":
    return "st"
    
  if nb_string[-1] == "2" and nb_string[-2:] != "12":
    return "nd"

  if nb_string[-1] == "3" and nb_string[-2:] != "13":
    return "rd"
  
  return "th"


def line_up(name, number):
  return f"{name}, you are the {number}{get_ending(number)} customer we serve today. Thank you!"

