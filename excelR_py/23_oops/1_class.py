# OOPS
# class

class info:
    name = "Xyz"

    def greet(self):
        print("Hi",self.name)   # pointer to name
        print("Hi",info.name)   # unchanged
        print(self.address)
 
i = info()
i.address = "FFFFF"     # dynamically added instance variable
i.greet()

i.name="Abc"             # self.name (overridden)
i.greet()