class Garden:
  def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
    self.diagrams = diagram.split("\n")
    self.students = sorted(students)
  
  
  PLANTS = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
  }
  

  def plants(self, student):
    student_index = self.students.index(student)
    
    return [
      self.PLANTS[self.diagrams[i][j]]
      for i in [0, 1]
      for j in [student_index * 2, student_index * 2 + 1]
    ]
    
  