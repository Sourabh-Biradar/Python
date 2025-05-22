# exercise 6 : oops

# 1
class Employee:
    def __init__(self,id,name,language):
        self.id=id
        self.name=name
        self.language=language
    def get_details(self):
        print(self.id,self.name,self.language)

class Developer(Employee):
    def get_language(self):
        print(f'{self.name} speaks {self.language}')

d=Developer(38,"Abc","French")
d.get_details()
d.get_language()

# 2
class Person:
    name = "Xyz"
    def get_name(self):
        return self.name

class Job:
    role="Senior Dev"
    def get_role(self):
        return self.role

class Employee(Person,Job):
    def display_info(self):
        print(self.get_name())
        print(self.get_role())

e=Employee()
e.display_info()

# 3
class A:
    def infoA(self):
        print("Class-A")
class B(A):
    def infoB(self):
        print("Class-B")
class C(B):
    def infoC(self):
        print("Class-C")

c = C()
c.infoA()
c.infoB()
c.infoC()

# 4
class Shape:
    def area(self):
        print("Shape")
class Circle(Shape):
    r=4
    def area(self):
        print("cirlce :",3.14*self.r*self.r)
class Square(Shape):
    l=5
    def area(self):
        print("Square:",self.l*self.l)

s=Square()
s.area()
c=Circle()
c.area()

# 5
class Vehicle:
    def info(self):
        print("Vehicle")

class Bike(Vehicle):
    def info(self):
        print("Bike")

class Car(Vehicle):
    def info(self):
        print("Car")

class Boat:
    def infoB(self):
        print("Boat")  

class AmbMotor(Car,Boat):
    def info(self):
        super().info()
        print("AmbMoto")

amb= AmbMotor()
amb.info()
amb.infoB()