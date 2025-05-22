# exercise 3

# time

import time

now = time.strftime("%H:%M:%S")
print(now)

t = int(time.strftime("%H"))

if (t>=22 or t<2):
    print("Good Night!")
elif (t>=6 and t<12):
    print("Good Morning!")
elif (t>=12 and t<4):
    print("Good AfterNoon!")
else :
    print("Good Evening!")