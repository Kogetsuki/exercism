class BufferFullException(BufferError):
  """Exception raised when CircularBuffer is full.

  message: explanation of the error.

  """
  def __init__(self, message="Circular buffer is full"):
    super().__init__(message)

class BufferEmptyException(BufferError):
  """Exception raised when CircularBuffer is empty.

  message: explanation of the error.

  """
  def __init__(self, message="Circular buffer is empty"):
    super().__init__(message)


class CircularBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.buffer = [None] * capacity
    

  def read(self):
    if all(x is None for x in self.buffer):
      raise BufferEmptyException()

    self.buffer.append(None)
    read = self.buffer.pop(0)
    
    
    return read
    

  def write(self, data):
    if None not in self.buffer:
      raise BufferFullException()
    
    empty_slot = self.buffer.index(None)
    self.buffer[empty_slot] = data
    

  def overwrite(self, data):
    if None in self.buffer:
      self.write(data)
    else:
      self.buffer.pop(0)
      self.buffer.append(data)


  def clear(self):
    self.buffer = [None] * self.capacity