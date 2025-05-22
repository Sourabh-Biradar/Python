# string
# string methods

# NOTE : strings are immutable ; methods return new string ; WON'T change existing strings

# len()
# len() returns length of string/array

print(len("Racer")) # 5

a = "Ferrari"
print(len(a)) # 7

l = len(a)
print(l) # 7

# upper() & lower()
# to upper case & to lower case

b = "small"
print(b.upper()) # SMALL

c = "CAPS"
print(c.lower()) # caps

d = "theHULK"
print(d.upper()) # THEHULK
print(d.lower()) # thehulk

# rstrip() : removes specified TRAILING chars (WON'T work on begining chars)

e = "@@superman@@"
print(e.rstrip("@")) # @@superman

# replace() : replaces all occurances with GIVEN string

print(e.replace("superman","batman")) # @@batman@@

print(e.replace("man","-woman")) # @@super-woman@@

f = "sss00sss"
print(f.replace("s","z"))

# split() : creates LIST from specified char

g = "pirates*are*real"
print(g)
print(g.split("*")) # ['pirates', 'are', 'real']

# capitalize() : first letter to Cap

h = "name"
print(h.capitalize()) # Name

i = "whats your fav movie? is it Py10 ?"
print(i.capitalize()) # Whats ; py10

# center() : makes string length to specified length by leaving spaces at begining

j = "eighty eight" 
print(len(j)) # 12
print(j.center(20)) #     eighty eight
print(len(j.center(20))) # total len 20

# count() : returns count of specified char/chars

k = "abcadgaaz"
print(k.count("a")) # 4

l = "bat ball wkts bat out runs"
print(k.count("bat")) # 2

# endswith() : returns bool if string ends with specified char/chars

m = "hello!!"
print(m.endswith("!")) # true
print(m.endswith("o")) # false
print(m.endswith("o!!")) # true

n = "hello John"
print(n.endswith("ll",1,4)) # true

# find() : returns index of char, -1 if not found

o = "is it colour red?"
print(o.find("it")) # 3 : index
print(o.find("our")) # 9
print(o.find("blue")) # -1 : in case of absence

# index() : returns index of char, valueError if not found

p = "is it colour blue ? is it ?"
print(p.index("is")) # 0 index
print(p.index("red")) # value err : substring nt found

# NOTE : read methods.md for more methods