# error handling 
# exception handling

# any error in `try` ,control goes to `except` prints `err`, try-except is exited
# rest of code is executed as usual without crashing code

# 1 : basic syntax
try :
     i = 10/0
except :
     print("some error")

# 2 : sprcific typr of error
try :
    i = 10/0
except ZeroDivisionError:
    print("Can't be divided by 0")

# 3 : general exception
try :
    i = 10/0
except Exception as err:
    print(err) # division by zero

print("Rest of code")

# specific exception handling
try : 
    j = [3,4]
    print(j[2])
    i = 10/0
except ZeroDivisionError :
    print("trying to divide by 0")
except IndexError :
    print("trying to access out of bound index")



