# @property

class Student:
    def __init__(self,name,marks):
        self.name = name
        self._marks = marks
    
    @property
    def marks(self):
        return f'marks : {self._marks}'
    
    @marks.setter
    def marks(self,value):
        if value>=0:
            self._marks=value
        else:
            raise ValueError ("marks cant be negetive")
        
s = Student("Zyx",72)
print(s.marks)  # no brackets

s.marks = 88    # setter
print(s.marks)

try:
    s.marks = -88    # setter for -ve value
except ValueError as e:
    print(e)