# exercise 1
# if-else

#1
units=int(input("Enter units consumed :"))

if units<=200:
    print("bill : inr zero")
elif units<=300 and units>200:
    print("bill : inr ",(units-200)*5)
else :
    print("bill : inr ",(units-200)*10)


#2
price=150000
print("For KA press 1")
print("For AP press 2")
print("For MA press 3")
state=int(input("Enter state code :"))

if state==1:
    print("Tax :",price*0.2)
elif state==2:
    print("Tax :",price*0.15)
elif state==3:
    print("Tax :",price*0.17)
else:
    print("Enter valid State code")