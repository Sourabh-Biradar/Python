# 2 operators

# arithmstic : + , - , * , / , % , // , **
print(10//4)  # int reminder
print(3**2)  # 3 power 2

# assignment : = ,+= , -= , /= , *= , %= , **=
c = "sea"
print (c)

d = 5
d %= 2  # d = d % 2
print (d)

e = 5
e **= 3  # e = e ** 3
print(e)

# logical  : and , or , not
# returns True or False

# Bitwise : &  |  ~  >>  <<
# refer notes
print(16&24)
print(16|24)
print(~7)
print(~8)
print(7>>2)
print(7<<2)

# special 
# identity : is , not is (checks fr SAME memory allocation)
x=10
y=10
print(id(x))
print(id(y))
print(x is y)
# membership : in , not in
msg = "hello"
z = 'l'
print(z in msg)