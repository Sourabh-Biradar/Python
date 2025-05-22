# Exception handling
# syntax & runtime erros

# way 1
try:
    a = 7/0
    print(a)
except:
    print("Cant divide by zero ")


# way 2 : specific exception
# comment out one error
try:
    i = [1,2,3]
    print(i[3])
    a = 7/0
    print(a)
except ZeroDivisionError:
    print("Cant divide by zero ")
except IndexError:
    print("Index error")


# way 3 : finally
# always runs (clean up, close files, etc.)
try:
    a = 7/1
    print(a)
except:
    print("Cant divide by zero ")
finally:
    print("End...")