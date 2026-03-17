class Node:
  def __init__(self, value, succeeding=None, previous=None):
    self.value = value
    self.prev = previous
    self.next = succeeding


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None


  def __len__(self):
    node = self.head
    length = 0

    while node is not None:
      length += 1
      node = node.next

    return length


  def __iter__(self):
    node = self.head

    while node is not None:
      yield node.value
      node = node.next


  def iter_nodes(self):
    node = self.head

    while node is not None:
      yield node
      node = node.next


  def push(self, value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
      self.tail = new_node

    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node


  def pop(self):
    if self.tail is None:
      raise IndexError("List is empty")

    node_to_pop = self.tail

    if self.tail.prev:
      self.tail = self.tail.prev
      self.tail.next = None
    else:
      self.head = None
      self.tail = None

    return node_to_pop.value


  def shift(self):
    if self.head is None:
      raise IndexError("List is empty")

    node_to_remove = self.head

    if self.head.next:
      self.head = self.head.next
      self.head.prev = None
    else:
      self.head = None
      self.tail = None

    return node_to_remove.value


  def unshift(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node

    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node


  def delete(self, value):
    for node in self.iter_nodes():
      if node.value == value:
        # Node is head
        if node.prev is None:
          self.head = node.next
          if self.head:
            self.head.prev = None

        else:
          node.prev.next = node.next

        # Node is tail
        if node.next is None:
          self.tail = node.prev
          if self.tail:
            self.tail.next = None

        else:
          node.next.prev = node.prev

        return

    raise ValueError("Value not found")
