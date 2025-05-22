# lambda functions

# single arg
area = lambda l : l*l
print(area(4))

# multiple args
sum = lambda a,b : a+b
print(sum(3,4))

# lambda as arg
def cube(fn,x):
    return fn(x)*x

print(cube(lambda x : x*x,3))