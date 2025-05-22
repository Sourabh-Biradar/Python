# Loops : for & while

#for
p = 'python'
for i in p:
    print(i)

# for ladder
l = ['Apple','Banana','Mango']
for i in l:
    print(i)
    for j in i:
        print(j)


# range
n=5
for i in range(n,51,n):
    print(i)

# break 
for i in range(4):
    print(i)
    break

# continue
for i in range(4):
    if i==2:
        continue
    print(i)