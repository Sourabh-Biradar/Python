# operator overloading

# Ex : overloading '-' , here s-s = s*s 
class Sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __sub__(self,other):
        return self.x * self.y
    
s = Sub(9,4)
r = s-s
print(r)

# ex 2 : dunno exapme it is

class Add:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return Add(self.x+other.x,self.y+other.y)
    
    # __sub__ : self.x - other.x,self.y - other.y
    # __mul__ : self.x * other.x,self.y * other.y

a1 = Add(3,5)
a2 = Add(4,7)
res = a1+a2

print(res.x)       # self.x+other.x
print(res.y)       # self.y+other.y

# __str__() : pass how python shud shud print res

