# regex : Regular expressions
# Patters to search,match or replace text

import re

text = "python, might be in top 10, programming languages : list 101"


# functions
pattern = r'\d+'         # r'\d+' , r'\D' ,r'o' , r'in' ...
f= re.findall(pattern,"my number 321 and 0987654321")
print(f)

s = re.search(r'top',text)
print(s)

sp = re.split(r',',text)
print(sp)

sub = re.sub(r'python','ruby',text)
print(sub)

m = re.match(r'python',text)
print(m)

# meta characters
a = re.search(r'[axe]',text)    # first occure of 'any one'
print(a)

b = re.search(r'[a]',text)
print(b)

c = re.search(r't.p',text)
print(c)

d = re.search(r'^p',text)
print(d)

e = re.search(r'101$',text)
print(e)

f = re.search(r'am+',text)
print(f)

# flags
f1 = re.search(r'[AMx]',text,re.I)   # Ignorecase
print(f1)

f2 = re.search(r'a',text,re.A)   # Ignorecase
print(f2)

f3 = re.search(r'\w{9}','i live in bengaluru')
print(f3)

f4 = re.sub(r'-',":","12-34-56")
print(f4)

