# set methods

s1 = {2,4,'a',0.12}
s2 = {0.12,'b',True}

# print(s1+s2) # TypeError: unsupported operand

# union()
print(s1.union(s2))
print(s2.union(s1))
# both are same (no duplicates)

# update()
s2.update(s1)
# add s1 items to s2 (no duplicates)

print(s1,s2)

s3 = {2,4,'a',0.12}
s4 = {0.12,'b',True}

# interseection()
print(s3.intersection(s4))
# gets COMMON items from both

# intersection_update()
s4.intersection_update(s3)
print(s4)
# updates s4 by replacing items with just Common items

s5 = {2,4,'a',0.12}
s6 = {0.12,'b',True}

# symmetric_difference()
print(s6.symmetric_difference(s5))
# s6 = (s6 + s5) - common items

# symmetric_difference_update()
s6.symmetric_difference_update(s5)
print(s6)
# new s6 = (s6 + s5) - common items

s7 = {2,4,'a',0.12}
s8 = {0.12,'b',True}
s9 = {4,'a'}

# isdisjoint()
print(s7.isdisjoint(s8))
# if common items present , returns FALSE

# issuperset() & issubset()
print(s7.issuperset(s9))
# if all items of s9 are present in s7 , thn its superset

print(s9.issubset(s7))
# True if s9 is sub set of s7

# add()
s10 = {'x','z'}
s10.add('y')
print(s10)
# adds item to set

# remove()
s10.remove('x')
print(s10)
# s10.remove('a') # KeyError
# removes/deletes specified item

# discard()
s10.discard('a')
# removes item if present , no keyerror

s11 = {'c','a','r'}

# pop()
itm = s11.pop()
print(s11,itm)
# pops last item , to see wt item was popped assign var to pop()

# del
# not a method but a KEYWORD
# deletes whole set

del s11
# print(s11) # NameError , since its deleted

# clear()
s10.clear()
print(s10)
# deletes all ITEMS from set ; prints `set()`

# check if item is present
if 4 in s9:
    print("present")
else : print("no")