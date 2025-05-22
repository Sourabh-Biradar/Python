# Type Casting 

# Type casting or type conversion is process of converting one data type into specified data type

# Explicit Casting : by coders' choice

a = "1" #str
b = '2' # str

print (a+b) # 12 : concat

print (int(a)+int(b)) # 3
# type casts "1" to int:1 & '2' to int:2 & adds up

c = "abc"
print(int(c)) # valueErr

# Implicit Casting : automatic by Python 

x = 3 # int
y = 5.5 # float

print(x+y) # auto type cast to float : 8.5

# int(), float(), str(), ord(), hex(), tuple(), set(), list(), dict()