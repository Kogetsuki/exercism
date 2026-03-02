class School:
    def __init__(self):
      self.roster_dict = {}
      self._added = []

    def add_student(self, name, grade):
      if name in self.roster_dict:
        self._added.append(False)
        return
      
      self._added.append(True)  
      self.roster_dict[name] = grade
      
      
    def roster(self):
      return sorted(
        self.roster_dict.keys(),
        key = lambda x: (self.roster_dict[x], x)
      )
      

    def grade(self, grade_number):
      return sorted(
        [
          student 
          for student, grade in self.roster_dict.items()
          if grade == grade_number
        ],
        key = lambda x: x
      )


    def added(self):
      return self._added
