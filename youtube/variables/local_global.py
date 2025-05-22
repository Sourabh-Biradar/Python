# local vs global variables

# 1
# local variable
# can only be accessed it that block of code
# are destroyed after code executed

def fn():
    var = 4
    print(f'local var = {var}')

fn()
# print(var) # NameError: name 'var' is not defined
# since its LOCAL to fn()

# 2
# global variable
# can be accessed in whole program 
# dont get destroyed

x = 9
def func():
    print(F'frm func() x = {x}')

func()
print(f'global x = {x}') 

# 3
# priority
# local over global
# make sure no local variables have same name as global
a = 8 

def f1():
    a = 'eight'
    print(f'f1() a = {a}') # 'eight'

f1()
print(f'global a = {a}') # 8

# 4
# `global` keyword
# change global from fn()

gv = True
print(f'before gv = {gv}') # True

def f2():
    global gv
    gv = False

f2()
print(f'after gv = {gv}') # False

# NOTE : avoid modifying `global variables` 
# avoid variable name conflict

