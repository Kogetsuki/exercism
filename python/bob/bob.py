def is_question(text):
  text = text.strip()
  return text.endswith('?')


def is_yelled(text):
  return text.isupper() and any(c.isalpha() for c in text)


def is_silence(text):
  return not text.strip()


def response(hey_bob):
  if is_silence(hey_bob):
    return "Fine. Be that way!"
  if is_question(hey_bob) and is_yelled(hey_bob):
    return "Calm down, I know what I'm doing!"
  if is_question(hey_bob):
    return "Sure."
  if is_yelled(hey_bob):
    return "Whoa, chill out!"
  return "Whatever."