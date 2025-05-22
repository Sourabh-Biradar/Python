# function arguments

# default args
# if args are NOT provided , it will take `a=3,b=4` as default args

def add(a=3,b=4):
    print("a =",a,"b =",b,"=",a+b)

add() # no args ; output : 7 
add(9,10) # 19
add(6) # a = 6 ; b = 4 
add(b=8) # a = 3 ; b = 8


# keyword args
# args are passed as `key=value` , so order doesnt matter

def multiply(a,b):
    print("a =",a,"b =",b,"=",a*b)

multiply(b=7,a=5) 

# required args
# mandatory to provide all args (in case of no default args)

def fn(x,y,z):
    print(x,y,z)

fn("One",2,3.0) # reqd. args
# fn() # TypeError : missing 3 args
# fn("One") # TypeError : missing 2 args

# variable-length arg

# as *tuple
def students(*name):
    print(type(name))
    for n in name:
        print(n)

students("Ram","Laxman","Bheem")

# as **dictionary
def phonebook(**contacts):
    print(type(contacts))
    print(contacts["name"],contacts["number"])

phonebook(name="Abc",number=9123)

# function as arg
def square (x):
    return x * x

def cube(fn,x):
    print(fn(x) * x) 

print(square(3))
cube(square,3)

