# sets : no duplicates , no index
# mutable : add , update , remove , discard
# unordered : pop() to prove

s1=set([3,6,2,7,7,0,3])

s={3,6,2,1}
print(s)

s.add(10)
print(s)

s.remove(10)
print(s)

s.remove(2)
print(s)

s.update([5,8,99])
print(s)

s.pop()
print(s)

s1.clear()
print(s1)


s2={5,7,9,10}
s3 = {-1,-4,10}

print(s3.union(s2))

print(s3.intersection(s2))

print(s3.difference(s2))

print(s3.symmetric_difference(s2))