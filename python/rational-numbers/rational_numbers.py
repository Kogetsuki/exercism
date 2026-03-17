from math import gcd

class Rational:
  def __init__(self, numer, denom):
    if denom == 0:
      raise ZeroDivisionError("Denominator cannot be zero")

    g = gcd(numer, denom)

    numer //= g
    denom //= g

    if denom < 0:
      numer = -numer
      denom = -denom

    self.numer = numer
    self.denom = denom


  def __eq__(self, other):
    return self.numer == other.numer and self.denom == other.denom


  def __repr__(self):
    return f'{self.numer}/{self.denom}'


  def __add__(self, other):
    new_numer = (self.numer * other.denom) + (self.denom * other.numer)
    new_denom = self.denom * other.denom

    return Rational(new_numer, new_denom)


  def __sub__(self, other):
    new_numer = (self.numer * other.denom) - (self.denom * other.numer)
    new_denom = self.denom * other.denom

    return Rational(new_numer, new_denom)


  def __mul__(self, other):
    new_numer = self.numer * other.numer
    new_denom = self.denom * other.denom

    return Rational(new_numer, new_denom)


  def __truediv__(self, other):
    if other.numer != 0:
      new_numer = self.numer * other.denom
      new_denom = self.denom * other.numer

      return Rational(new_numer, new_denom)


  def __abs__(self):
    return Rational(abs(self.numer), abs(self.denom))


  def __pow__(self, power):
    if isinstance(power, int):
      if power > 0:
        return Rational(self.numer**power, self.denom**power)

      if power < 0:
        m = abs(power)
        return Rational(self.denom**m, self.numer**m)

      return Rational(1, 1)

    elif isinstance(power, float):
      return Rational(self.numer**power, self.denom**power)

    elif isinstance(power, Rational):
      pass


  def __rpow__(self, base):
    if self.denom == 1:
      return base ** self.numer

    if base < 0 and self.denom % 2 == 1:
      return -((-base) ** (self.numer / self.denom))

    return base ** (self.numer / self.denom)
