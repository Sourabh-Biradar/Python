# dictionary

# ordered
# key : value pairs

d = {"one" :1,'two':2,'three':3}

print(d)

# access values
print(d['two'])
# print(d['four']) # KeyError

print(d.get('one'))
print(d.get('four')) # None

# access keys & values
print(d.keys())
print(d.values())
# dict_keys(['one', 'two', 'three'])
# dict_values([1, 2, 3])

# items
print(d.items())
# dict_items([('one', 1), ('two', 2), ('three', 3)])

for key,val in d.items():
    print(key,val)

# print all values
for v in d:
    print(d[v])



