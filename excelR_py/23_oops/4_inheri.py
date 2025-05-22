# inheritance : type of oops
# parent class used by child class

# single inheritance : one P one C
class Father():
    def display(self):
        print("Father class")

class Son(Father):     #inheritance 
    def display(self):
        super().display()    # if not Son.display() overrides Father.display()
        print("Son class")

obj = Father()
obj.display()

obj1 = Son()
obj1.display()

# multi-inheritance : multi P one C
class P1:
    def info1(self):
        print("P1")
class P2:
    def info2(self):
        print("P2")
class C(P1,P2):
    pass

ch = C()
ch.info1()
ch.info2()

# multi-level : GrandP >> P >> C
class GrandP:
    def infoGP(self):
        print("Grand Parent")
class P(GrandP):
    def infoP(self):
        print("Parent")
class C(P):
   pass

ch1 = C()
ch1.infoGP()
ch1.infoP()

# hierarchical : one P multiple C
class Father:
    def infoF(self):
        print("Father")
    
class Son(Father):
    pass

class Daughter(Father):
    pass

s=Son()
s.infoF()
d=Daughter()
d.infoF()

# hybrid : combo of more than one types
# ex: multiple + hierarchical
class GrandPaa:
    def infoGP(self):
        print("Hybrid GrandPaa")

class Father(GrandPaa):
    def infoF(self):
        print("Hybrid Father")

class Mother:
    def infoM(self):
        print("Hybrid Mother")

class Son(Father):
    pass

class Daughter(Father,Mother):
    pass

s=Son()
s.infoF()
s.infoGP()

d=Daughter()
d.infoGP()
d.infoF()
d.infoM()