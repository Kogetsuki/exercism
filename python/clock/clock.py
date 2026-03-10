class Clock:
  def __init__(self, hour, minute):
    total = (hour * 60 + minute) % (24 * 60)
    self.hour = total // 60
    self.minute = total % 60
    

  def __repr__(self):
    return f"Clock({self.hour}, {self.minute})"


  def __str__(self):
    return f"{self.hour:02}:{self.minute:02}"
    

  def __eq__(self, other):
    if not isinstance(other, Clock):
      return NotImplemented
    return self.hour == other.hour and self.minute == other.minute    


  def __add__(self, minutes):
    return Clock(self.hour, self.minute + minutes)

  def __sub__(self, minutes):
    return Clock(self.hour, self.minute - minutes)
