# 3 Data types

# primitive : int , float , complex , str , Bool , None
# non - primitive : list , tuple , set , dict , range

print(type(32))
print(type(-22.3))
print(type(3+5j))
print(type("hi"))
print(type(True))
print(type(None)) # NoneType

a=[3,5.1,'a']
b=(3,4,5,3,0)
c=set(b)
d={1:'a',2:'b'}
e="hey"
f=range(0,5)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))