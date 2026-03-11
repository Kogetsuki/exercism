class EmptyListException(Exception):
  def __init__(self, message="The list is empty."):
    super().__init__(message)


class Node:
  def __init__(self, value):
    self._value = value
    self._next = None


  def value(self):
    return self._value 


  def next(self):
    return self._next


class LinkedList:
  def __init__(self, values=None):
    self._head = None
      
    if values:
      for value in values:
        self.push(value)


  def __iter__(self):
    node = self._head

    while node is not None:
      yield node.value()
      node = node.next() 


  def __len__(self):
    node = self._head
    length = 0
    
    while node is not None:
      length += 1
      node = node.next()
      
    return length


  def head(self):
    if self._head is None:
      raise EmptyListException()
    return self._head
    

  def push(self, value):
    new_node = Node(value)
    new_node._next = self._head
    self._head = new_node


  def pop(self):
    if len(self) == 0:
      raise EmptyListException()
    
    to_pop = self.head().value()
    self._head = self.head().next()

    return to_pop
  

  def reversed(self):
    return [
      node
      for node in self
    ][::-1]
