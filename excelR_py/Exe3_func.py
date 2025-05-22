# exercise 3
# functions

# convert c to f
def wcal(c):
    f = (c * 9/5) + 32
    return f'Fahrenheit :{f}'

print(wcal(25))

# convert f to c
wapp = lambda f : (f - 32) * 5/9

print('celsius :',wapp(77))

# fibo
def fibo(a,b):
    for i in range(6):
        temp = a+b
        a=b
        b=temp
        print(temp)

fibo(0,1)