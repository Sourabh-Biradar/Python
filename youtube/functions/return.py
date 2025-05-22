# return

# returns functions output

def add(a,b):
    return a+b

result = add(4,5) # result var holds return value
print(result)

def sub(a,b):
    return a-b

print(sub(9,2)) # or we can also deirectly print func output

def div(a,b):
    return "uhh"
    return a/b

print(div(3,1)) # uhh ; returns first return value

# multiple return
# returned as tuple

def person():
    name="Abc"
    age = 22
    city = "Bluru"
    return name,age,city

p_name,p_age,p_city = person()
print(p_name)
print(p_age)
print(p_city)
