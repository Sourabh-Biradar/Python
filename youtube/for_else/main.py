# for-else loop

# else is executed once all iterations are over
# basically, when for(cond.) == false
# after else is executed , loop is exited

# can also n used with `WHILE LOOP`

for i in range(5):
    print(i)
else : print("last iteration done")

# break
for j in range(5):
    print(j)
    if j==3:
        break
else:print("last iteration done")
# break : breaks out of whole for-else loop