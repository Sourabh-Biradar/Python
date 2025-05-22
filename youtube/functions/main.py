# functions

# Block of code tht performs specific task
# it is reusable

# user-defined function

def greet():
    print("Hey!")

greet() # func call

def cal_mean(a,b):
    mean = (a+b)/2
    print(mean)

x = 4
y = 6
cal_mean(x,y) # calling func by passing args

cal_mean(11,5) # calling func by passing args

def greater(i,j):
    if (i>j):
        print(i ,"is greater")
    else:
        print(j,"is greater")

greater(5,9)

# built-in functions
# no need to use `def`
# range(), len(), print() etc.
