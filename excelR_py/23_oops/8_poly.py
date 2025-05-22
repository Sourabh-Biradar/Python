# polymorphism : obj can act in may ways
# duck typing : DT checked at runtime , doesnt matter actual type

class Bike:
    def brand(self):
        return "Yahama"

class Car:
    def brand(self):
        return "Mahindra"

def info(vahicle):              # We don't care whether it's Duck/Car/Bike
    print(vahicle.brand())  

c=Car()
b=Bike()
info(c)      # Car.brand()
info(b)      # Bike.brand()

# exapmle 2
class Circle:
    def area(self):
        return 'area : pi*r*r'
class Square:
    def area(self):
        return 'area : a*a'

def area(shape):              # func poly using duck typing
    print(shape.area())

c= Circle()
s= Square()

area(c)
area(s)