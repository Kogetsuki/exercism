COLORS_LIST = {
  "black": 0,
  "brown": 1,
  "red": 2,
  "orange": 3,
  "yellow": 4,
  "green": 5,
  "blue": 6,
  "violet": 7,
  "grey": 8,
  "white": 9
}


TOLERANCE = {
  "grey": 0.05,
  "violet": 0.1,
  "blue": 0.25,
  "green": 0.5,
  "brown": 1,
  "red": 2,
  "gold": 5,
  "silver": 10,
}


def resistor_label(colors):
  if len(colors) == 1:
    return "0 ohms"
    
  if len(colors) == 4:
    value_digits = colors[:2]
    multiplier_color = colors[2]
    tolerance_color = colors[3]
    
  else:
    value_digits = colors[:3]
    multiplier_color = colors[3]
    tolerance_color = colors[4]

  number = int(''.join(str(COLORS_LIST[c]) for c in value_digits))
  number *= 10 ** COLORS_LIST[multiplier_color]

  if number >= 1000000:
    value = number / 1000000
    unit = "megaohms"
  elif number >= 1000:
    value = number / 1000
    unit = "kiloohms"
  else:
    value = number
    unit = "ohms"

  if isinstance(value, float) and value.is_integer():
    value = int(value)

  tolerance = TOLERANCE[tolerance_color]

  return f"{value} {unit} ±{tolerance}%"