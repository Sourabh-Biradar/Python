# 4 List

l = [8,-2,'a',3.7]

#negative index : -4 -3 -2 -1
print(l[-4])  

#multidimention
l1 = [3,[4,5,6],['a','x']]
print(l1[2][1])
print (l1[-2][-1])

# slicing : [start:stop:step]
print(l[1::2])

# methods 

l.append(6)
l.append([3,4,5])
print(l)

l.extend([9,8,7])
print(l)

l.insert(1,'one')
print(l)

l.remove([3,4,5])
print(l)

l.pop()
print(l)

l.pop(2)
print(l)

l1.clear()
print(l1)

print(l.index('a'))

print(l.count(8))

l.reverse()
print(l)

l2 = [5,2,-9,0,1]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)


# copy : shallow & deep
# deep copy : any changes to 'l' reflect in 'l3' (NOT Recmd)
l3 = l
print(l3)
l.append(99)
print(l3)

# shallow copy
l4 = l.copy()
print(l4)
l.append('last')
print(l4)

# delete : non-existant
del l3
del l4
print(l3,l4)