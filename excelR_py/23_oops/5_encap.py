# encapsulation : public, private, protected

class Person:
    def __init__(self,name,age,flat):
        self.name=name                  # public
        self._age=age                   # protected
        self.__flat=flat                # private

    def info(self):
        print(self.name)
        print(self._age)
        print(self.__flat)
class Govt(Person):
    pass

p = Person("Abc",22,"F-101")
p.info()
print(p.name)    # public,protected,private

g=Govt("Abc",22,"F-101")
g.info()         # protected
print(p._age)    # protected (bt nt recmd)
print(g._age)    # protected (bt nt recmd)

print(p.__flat)  # private : AttErr
print(p._Person__flat)  # Trick
