# Tuple : immutable 

t= (3) #int
t = (3,) #tuple
t = (3,'three')

t1 = 1,2,3,'four'
print(type(t1))

# t[0] = 3 # error : immutable

# remove duplicates
t2= 9,9,9,9,8
t3 = set(t2)
print(t3,type(t3))

