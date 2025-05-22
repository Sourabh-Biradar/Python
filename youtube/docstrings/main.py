# docstrings
# document string
# unlike comments ths WON'T be ignored

# syntax : func.__doc__ 

def square(n):
    '''This function accepts an integer 
    & returns square of that integer'''
    return (n**2)

print(square(4))

print(square.__doc__)
# prints docstring

# NOT docstring
def fn():
    print("!!")
    """NOW THIS AIN'T DOCSTRING
    instead prints None"""
    
print(fn.__doc__) # None