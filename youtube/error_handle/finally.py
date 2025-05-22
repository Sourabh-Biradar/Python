# finally clause

# try :
# except :
# finally :

# `finally` block always executes , may code execute `try` or `except`

def fn(a):
    try:
        l = [9,8,7]
        return l[a]
    except:
        return f'{a} out of bound index'
    finally:
        print("finally clause executed")
    

print(fn(5))

# why finally
def fn(a):
    try:
        l = [9, 8, 7] 
        return l[a]
    except:
        return f'{a} out of bound index'
    
    print("this print statement doesn't execute as fn is returned")

print(fn(5))

def fn(a):
    try:
        l = [9, 8, 7]  
        return l[a]
    except:
        return f'{a} out of bound index'
    finally:
        print('finally clause executed')
        # ths will execute even though fn returned

print(fn(5))
