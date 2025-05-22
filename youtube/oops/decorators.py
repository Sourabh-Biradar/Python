# OOPs

# Decorators 
# function that modifies/wraps the behavior of another function / method

def greet(fx):
    def mfx(*args, **kwargs):
        print("Greetings,Thanks for choosing us")
        fx(*args, **kwargs)
        print('Visit again soon')
    return mfx

@greet # decorator
def tkts(qty):
    print(f'Total amount for {qty} persons {180*qty}')

tkts(4)

# without @greet 
def err(code):
    print(F'OOPS !! Something went wrong . Error code:{code}')

greet(err)(423)



    
