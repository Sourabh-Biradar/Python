# enumerate function
# enum

for i in enumerate(range(5,10)):
    print(i)
# prints tuple : (index,value)


cars = ['Harriar','Thar','XUV 700']
for i,car in enumerate(cars):
    print(i,car)
# prints : index value

# start
primes = (1,2,3,5,7,11)
for idx,prime in enumerate(primes,start=3):
    print(idx,prime)
# index : stats from 3; values will b printed frm 1 to 11