# dictionary : dict
# key-value ,unordered , mutable

d={1:'one',2:'two','ten':10}
print(d)

d1 = dict(name='Abc',age=22,city="Bluru")
d2 = {'name':'Xyz','age':20,'city':'Goa'}

print(d1.keys())
print(d2.values())

print(d1['age'])

print(d1.get('name'))

print(d1.items())

d1.update(d)
print(d1)

d1.pop('ten')
print(d1)

d1.popitem()
print(d1)

