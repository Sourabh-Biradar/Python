# sets

# unordered collection of UNIQUE items
# ordered not guarenteed
# items are immutable

s = {2,4,2,0,1,9,1}
print(type(s),s)

s1 = {'set',False,-2,8,'a'}
print(s1)

# creating empty set
empty_set = set()
print(type(empty_set))

# access items
for item in s1:
    print(item)

# indexing
print(s1[2]) # TypeError: 'set' object is not subscriptable

