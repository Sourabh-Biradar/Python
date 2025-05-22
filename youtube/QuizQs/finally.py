# finally clause


def fn(a):
    try:
        l = [9, 8, 7]  # This block is properly indented
        return l[a]
    except:
        return f'{a} out of bound index'
    finally:
        return 'finally clause executed'

print(fn(5))


# `finally` return OVERRIDES other returns
# so, fn() ALWAYS returns 'finally clause executed'
# rather print finally clause
# AVOID return


# why finally
def fn(a):
    try:
        l = [9, 8, 7]  # This block is properly indented
        return l[a]
    except:
        return f'{a} out of bound index'
    
    print("this print statement doesn't execute as fn is returned")

print(fn(5))

def fn(a):
    try:
        l = [9, 8, 7]  # This block is properly indented
        return l[a]
    except:
        return f'{a} out of bound index'
    finally:
        print('finally clause executed')
        # ths will execute even though fn returned

print(fn(5))


