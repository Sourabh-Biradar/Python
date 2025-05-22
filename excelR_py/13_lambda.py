# lambda functions / anonymous fn

a = lambda : print("hii")
a()

b = lambda greet : print(greet)
b("Hello")

c = lambda a,b : print(a+b)
c(3,4)

# if-else
largest = lambda a,b : a  if a>b else b
print(largest(10,4))

# sort
# 'key' parameter in sort() / sorted() what value to use to determine their sort order

l = ["Ask","a","xx","E"]
l.sort(key = lambda x :len(x))
print(l)


# map (fn,sequence)
l1 = [1,2,3,4]
sq = list(map(lambda x : x*x , l1))
print(sq)


# map,filter : simplified
def fn(x):
    return x+5

l= [3,5,7,9]
f = list(map(fn,l))
print(f)

# fn : pass the func
# fn() : call the func