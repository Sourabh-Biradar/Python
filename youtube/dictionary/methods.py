# dictionary methods

d1 = {1 : ['o','n','e'], 2 : ['t','w','o']}
d2 = {0 : ['z','e','r','o']}
d3 = {10 : ['t','e','n']}

# update()
d1.update(d2)
print(d1)
# new d1 = d1 + d2

# clear()
d3.clear()
print(d3) # {}

# pop()
d1.pop(0)
print(d1) 
# `0` key : value popped

# popitem()
d1.popitem()
print(d1)
# last pair delete

d4 = {'a':'A','b':'B','c':'C'}
# del 
del d4['b']
print(d4) 
# del specified pair

del d1
print(d1) # NameError
# del whole dict
