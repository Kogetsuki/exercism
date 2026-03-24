class Zipper:
  def __init__(self, focus, path):
    self.focus = focus
    self.path = path


  @staticmethod
  def from_tree(tree):
    return Zipper(tree, [])


  def value(self):
    return self.focus["value"]


  def set_value(self, new_value):
    new_focus = {
      "value": new_value,
      "left": self.focus["left"],
      "right": self.focus["right"]
    }

    return Zipper(new_focus, self.path)


  def left(self):
    if self.focus["left"] is None:
      return None

    new_focus = self.focus["left"]
    new_path = ("left", self.focus["value"], self.focus["right"])

    return Zipper(new_focus, self.path + [new_path])


  def set_left(self, new_left):
    new_focus = {
      "value": self.focus["value"],
      "left": new_left,
      "right": self.focus["right"]
    }

    return Zipper(new_focus, self.path)


  def right(self):
    if self.focus["right"] is None:
      return None

    new_focus = self.focus["right"]
    new_path = ("right", self.focus["value"], self.focus["left"])

    return Zipper(new_focus, self.path + [new_path])


  def set_right(self, new_right):
    new_focus = {
      "value": self.focus["value"],
      "left": self.focus["left"],
      "right": new_right,
    }

    return Zipper(new_focus, self.path)



  def up(self):
    if not self.path:
      return None

    direction, parent_value, sibling = self.path[-1]

    if direction == "left":
      new_focus = {
        "value": parent_value,
        "left": self.focus,
        "right": sibling
      }

    else:
      new_focus = {
        "value": parent_value,
        "left": sibling,
        "right": self.focus
      }

    return Zipper(new_focus, self.path[:-1])


  def to_tree(self):
    z = self
    while z.path:
      z = z.up()

    return z.focus
