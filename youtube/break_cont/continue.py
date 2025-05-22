# continue statement

# SKIPS iteration & CONTINUES with the loop

for i in range(10):
    if (i == 5):
        print("Skips 5")
        continue
    print(i)

# prints 1,2,3,4 ; skips 5 ; continues printing 6,7,8,9 
    