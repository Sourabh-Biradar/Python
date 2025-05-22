# tuple methods
# NOTE : convert tuple to list to manipulte & after tht revert to tuple

# convert
t = (1,3,5,'7')
l = list(t) 

# append()
l.append(None)
print(l)

# change
l[4] = True
print(l)

# pop() : deletes last elem
l.pop()
print(l)

# concat
t2 = ('a','b','c')
t3 = t + t2
print(type(t3),t3)

# tuple.count()

# tuple.index() ; if not found valueError




