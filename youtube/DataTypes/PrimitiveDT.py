# Primitive Data types

# int
a = 1

# str
b = "b" 
c = 'c' 
z = '44'
y = "3.06"

# bool
d = True 
e = False
# 'T' & 'F' caps

# float
f = 12.88 

# None
n = None 
# null , absence of value

# complex
g = 3 + 8j 
# 3 real part & 8 imaginary part
# j & J NOT i for imaginary part

h = complex(4,5) 
print(h) # (4+5j)

# type() gives data type of variable
print("Data type :",type(b)) # < class 'str' >

print(a+b) # typeErr : int + str  invalid

print(b+c) # valid : bc (concat)

# NOTE : comment out errors before running code!!