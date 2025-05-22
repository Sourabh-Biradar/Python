# is
# comparsion operator
# is vs ==

a = 4 
b = 4
print(a == b) # value

print(a is b) # memory location
print(id(a),id(b)) # same (None, str, int, float, tuple immutable)

c = [1,2,3]
d = [1,2,3]
print(c == d) # True
print(c is d) # False
print(id(c),id(d)) # different (list, dict)

