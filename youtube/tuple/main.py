# tuple
# immutable list

t = (2,4,6,'8')
print(type(t),t)
print(t[2])

# [ ] = list ; (,) = tuple
#  var = ("x") = string ; var = ("x",) = tuple
# COMMA must

t1 = (2) # int
t2 = (2,) # tuple
t3 = [2] # list

print(type(t1),type(t2),type(t3))

# immutable
t[0] = 1
print(t) # TypeError: 'tuple' object does not support item assignment



