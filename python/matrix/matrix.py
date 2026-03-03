class Matrix:
  def __init__(self, matrix_string):
    self.matrix = matrix_string


  def row(self, index):
    rows = self.matrix.split("\n")
    return [
      int(x)
      for x in rows[index - 1].split()
    ]
    

  def column(self, index):
    split_rows = [
      row.split()
      for row in self.matrix.split("\n")
    ]

    return [
      int(split_row[index - 1])
      for split_row in split_rows
    ]