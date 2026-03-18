class CustomSet:
  def __init__(self, elements=[]):
    self.elements = []

    for el in elements:
      if el not in self.elements:
        self.elements.append(el)


  def __iter__(self):
    return iter(self.elements)


  def isempty(self):
    return not self.elements


  def __contains__(self, element):
    return element in self.elements


  def issubset(self, other):
    return all(
      x in other
      for x in self.elements
    )


  def isdisjoint(self, other):
    return all(
      x not in other
      for x in self.elements
    )


  def __eq__(self, other):
    return sorted(self.elements) == sorted(other)


  def add(self, element):
    if element not in self.elements:
      self.elements.append(element)


  def intersection(self, other):
    data = [
      x
      for x in self.elements
      if x in other
    ]

    return CustomSet(data)


  def __sub__(self, other):
    data = [
      x
      for x in self.elements
      if x not in other
    ]

    return CustomSet(data)


  def __add__(self, other):
    return CustomSet([*self.elements, *other])
