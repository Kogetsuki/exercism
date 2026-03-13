class Scale:
  def __init__(self, tonic):
    self.tonic = tonic
    self.scale = (
      self.FLATS
      if tonic in self.FLAT_KEYS
      else self.SHARPS
    )


  SHARPS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
  FLATS = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

  FLAT_KEYS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]


  def chromatic(self):
    i = self.scale.index(self.tonic)
    return self.scale[i:] + self.scale[:i]


  def interval(self, intervals):
    self.tonic = self.tonic[:1].upper() + self.tonic[1:]

    diatonic = [self.tonic]

    i = self.scale.index(self.tonic)
    for step in intervals:
      if step == "m":
        i += 1
      elif step == "M":
        i += 2
      elif step == "A":
        i += 3

      i %= len(self.scale)

      diatonic.append(self.scale[i])

    return diatonic
