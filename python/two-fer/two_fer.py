def two_fer(name=""):
  to_say = (
    name
    if name
    else "you"
  )
  
  return f"One for {to_say}, one for me."