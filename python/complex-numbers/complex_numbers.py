import math

class ComplexNumber:
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary


  # Convert real number into ComplexNumber instance
  def coerce(self, other):
    if isinstance(other, (int, float)):
      return ComplexNumber(other, 0)

    return other


  def __eq__(self, other):
    other = self.coerce(other)

    return (
      isinstance(other, ComplexNumber) and
      other.real == self.real and
      other.imaginary == self.imaginary
    )


  def __add__(self, other):
    other = self.coerce(other)

    new_real = self.real + other.real
    new_imaginary = self.imaginary + other.imaginary

    return ComplexNumber(new_real, new_imaginary)


  def __radd__(self, other):
    return self + other


  def __mul__(self, other):
    other = self.coerce(other)

    new_real = (self.real * other.real) - (self.imaginary * other.imaginary)
    new_imaginary = (self.imaginary * other.real) + (self.real * other.imaginary)

    return ComplexNumber(new_real, new_imaginary)


  def __rmul__(self, other):
    return self * other


  def __sub__(self, other):
    other = self.coerce(other)

    new_real = self.real - other.real
    new_imaginary = self.imaginary - other.imaginary

    return ComplexNumber(new_real, new_imaginary)


  def __rsub__(self, other):
    return ComplexNumber(other, 0) - self


  def __truediv__(self, other):
    other = self.coerce(other)

    first_num = (self.real * other.real) + (self.imaginary * other.imaginary)
    second_num = (self.imaginary * other.real) - (self.real * other.imaginary)
    denominator = other.real**2 + other.imaginary**2

    return ComplexNumber(first_num / denominator, second_num / denominator)


  def __rtruediv__(self, other):
    return ComplexNumber(other, 0) / self


  def __abs__(self):
    return math.sqrt(self.real**2 + self.imaginary**2)


  def conjugate(self):
    return ComplexNumber(self.real, -self.imaginary)


  def exp(self):
    new_real = math.exp(self.real) * math.cos(self.imaginary)
    new_imaginary = math.exp(self.real) * math.sin(self.imaginary)

    return ComplexNumber(new_real, new_imaginary)
