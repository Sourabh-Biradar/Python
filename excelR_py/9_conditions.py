# condition statements : if , if-else , elif ladder

#if
num=8
if num%2==0 :
    print(num ,": is divisible by 2")


# if-else
if num%3==0 :
    print(num ,": is divisible by 3")
else : 
    print(num ,": is not divisible by 3")

# isinstance(data,dt)
v = 3.4
if isinstance(v,float):
    print("its float")
else:
    print('not a float')

# elif ladder 
n=25
 
if n%2==0 :
    print(n ,": is divisible by 2")
elif n%3==0:
    print(n ,": is divisible by 3")
elif n%5==0:
    print(n ,": is divisible by 5")
else : 
    print(n ,": is not divisible by 2,3,5")