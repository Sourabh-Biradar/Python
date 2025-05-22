# OOPs
# object oriented programming
# classes , objects , instance , self

# NOTE : class name starts with CAPS

class Student:
    name = 'Abc'
    roll = 38
    marks = [{'Eng':93},{'Math':78},{'Sci':88}]

s = Student()

# access fields
print(f'marks :{s.marks}')

# change fields
s.roll = 28
print(f'new roll number :{s.roll}')

# function in class
class Person:
    name = 'Lmn'
    age = 24
    def info(self):
        print(f'{self.name} is {self.age} years old.')

p = Person()
p.info()
# p = object / instance
# info() = instance method ; needs instance (p) to be called

# self = current instance of class
p1 = Person()
p1.name = 'Lmn'
p1.info()
# self = p for p.info & p1 for p1.info()

# advanced
class Player:
    def stats(self):
        name = self.name
        runs = self.runs
        wkts = self.wkts
        print(f'Player {name} has scored {runs} & took {wkts} wkts')

player1 = Player()
player1.name = "Abc"
player1.runs = 76
player1.wkts = 2
player1.stats()

player2 = Player()
player2.name = "Xyz"
player2.runs = 9
player2.wkts = 4
player2.stats()
# use constructors 