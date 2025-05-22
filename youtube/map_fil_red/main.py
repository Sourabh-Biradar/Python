# map , filter & reduce

l = [1,3,5,-7]

# map 
# syntax : map(fn,iterable)
def square(x):
    return x*x

listsq = map(square,l)

print(listsq) # <map object at 0x1060ad960>
print(list(listsq)) # [1, 9, 25, 49]

# filter
# filter(True fn,iterable)
def filFn(a):
    return a>2 # True or False

newl = filter(filFn,l)

print(newl) # <filter object at 0x109af5c00>
print(list(newl)) # [3, 5]

# reduce
# reduce(fn,iterable)
# from functools import reduce

from functools import reduce

sub = lambda x,y : x - y

nums = [9,7,5,3,1]

print(reduce(sub,nums)) # -7

# 9-7; 2-5; -3-3; -6-1 = -7



