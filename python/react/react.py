class InputCell:
  def __init__(self, initial_value):
    self._value = initial_value
    self.listeners = []


  @property
  def value(self):
    return self._value


  @value.setter
  def value(self, new_value):
    if self._value == new_value:
      return
    self._value = new_value

    # Notify listeners
    affected_cells = []
    self._propagate(affected_cells)

    # Trigger callbacks
    for cell in affected_cells:
      cell._fire_callbacks()


  def _propagate(self, affected_cells):
    for listener in self.listeners:
      listener._update(affected_cells)


class ComputeCell:
  def __init__(self, inputs, compute_function):
    self.inputs = inputs
    self.compute_function = compute_function
    self.listeners = []
    self.callbacks = set()

    # Initial computation
    self._value = self.compute_function([
      input.value
      for input in self.inputs
    ])

    self._last_callback_value = self._value

    # Register a listener to all inputs
    for input in self.inputs:
      input.listeners.append(self)


  @property
  def value(self):
    return self._value


  def _update(self, affected_cells):
    new_value = self.compute_function([
      input.value
      for input in self.inputs
    ])

    # Propagate
    self._value = new_value

    if self not in affected_cells:
      affected_cells.append(self)

    for listener in self.listeners:
      listener._update(affected_cells)


  def _fire_callbacks(self):
    if self._value != self._last_callback_value:
      for callback in list(self.callbacks):
        callback(self._value)

      self._last_callback_value = self._value


  def add_callback(self, callback):
    self.callbacks.add(callback)


  def remove_callback(self, callback):
    if callback in self.callbacks:
      self.callbacks.remove(callback)
