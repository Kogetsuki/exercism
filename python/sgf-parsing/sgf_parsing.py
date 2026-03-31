class SgfTree:
  def __init__(self, properties=None, children=None):
    self.properties = properties or {}
    self.children = children or []


  def __eq__(self, other):
    if not isinstance(other, SgfTree):
      return False

    return (
      self.properties == other.properties and
      self.children == other.children
    )


  def __ne__(self, other):
    return not self == other


def parse(input_string):
  if not input_string:
    raise ValueError("tree missing")

  input_string = input_string.strip()
  if not input_string.startswith("(") or not input_string.endswith(")"):
    raise ValueError("tree missing")

  index = 0
  length = len(input_string)

  def parse_tree():
    nonlocal index
    if input_string[index] != "(":
      raise ValueError("tree missing")
    index += 1  # skip '('

    nodes = []
    while index < length and input_string[index] != ")":
      if input_string[index] == ";":
        nodes.append(parse_node())

      elif input_string[index] == "(":
        # Child tree belongs to last node
        if not nodes:
          raise ValueError("tree with no nodes")
        nodes[-1].children.append(parse_tree())

      else:
        raise ValueError("tree missing")

    if not nodes:
      raise ValueError("tree with no nodes")


    for i in range(len(nodes) - 1):
      nodes[i].children.append(nodes[i + 1])

    index += 1  # skip ')'
    return nodes[0]

  def parse_node():
    nonlocal index
    if input_string[index] != ";":
      raise ValueError("tree missing")
    index += 1

    properties = {}
    while index < length and input_string[index] not in ";()":
      # Parse key
      start = index
      while index < length and input_string[index].isalpha():
        index += 1

      key = input_string[start:index]
      if not key:
        raise ValueError("properties without delimiter")
      if not key.isupper():
        raise ValueError("property must be in uppercase")

      # Parse values
      values = []
      while index < length and input_string[index] == "[":
        index += 1  # skip '['
        val = []

        while index < length and input_string[index] != "]":
          c = input_string[index]
          if c == "\\":
            index += 1
            if index >= length:
              break

            next_c = input_string[index]
            if next_c == "\n":
              index += 1  # Remove escaped newline
              continue

            elif next_c in "\t\r\f":
              val.append(" ")

            else:
              val.append(next_c)

            index += 1

          elif c in "\t\r\f":
            val.append(" ")
            index += 1

          else:
            val.append(c)
            index += 1

        if index >= length or input_string[index] != "]":
          raise ValueError("properties without delimiter")

        index += 1  # skip ']'
        values.append("".join(val))

      if not values:
        raise ValueError("properties without delimiter")
      properties[key] = values

    return SgfTree(properties=properties)

  tree = parse_tree()
  if index != length:
    raise ValueError("tree missing")

  return tree
