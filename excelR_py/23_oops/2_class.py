# static & dynamic

# static
class Car :
    brand = "BMW"
    model = "Z4"
    year = 2024

    def car_info(self):
        print(f'{self.brand}-{self.model}')

c = Car()
c.car_info()

# dynamic vars : inside --init--()
class Bike:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def bike_info(self):
        print(f'{self.brand}-{self.model}')

b1=Bike("Ducati","V4")
b1.bike_info()

b2=Bike("Yamaha","R1")
b2.bike_info()