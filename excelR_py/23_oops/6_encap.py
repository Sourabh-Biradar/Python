# encapsulation : getter & setter

class Abc:
    def __init__(self,salary):
        self.__salary=salary
    
    def get_salary(self):          # getter
        return self.__salary
    
    def set_salary(self,amount):   # setter
        if amount>0:
            self.__salary=amount
        else :
            print("invalid salary amount")

a = Abc(50000)
print(a.get_salary())

a.set_salary(75000)
print(a.get_salary())