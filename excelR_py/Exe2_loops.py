# Exercise 2
# for & while

# skip even , break on 15
# while
a = 0
while a<20:
    a+=1
    if a%2==0:
        continue
    if a==15:
        break
    print(a)

# for
print("for")
for i in range(20):
    if i%2==0:
        continue
    if i==15:
        break
    print(i)

# user input until 'exit' or empty string, skip blank spaces
inp=input("Enter string :")
while True:
    if inp=='exit' or inp =="":
        break
    inp=input("Enter string :")
    if inp==" ":
        continue

# count nums until multiple of 7 , skip 4
count = 0
for i in range(1,20):
    if i == 4:
        continue
    if i % 7 == 0:
        break
    count += 1
    print(i)
print("count :",count)