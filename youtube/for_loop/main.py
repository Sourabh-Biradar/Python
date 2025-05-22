# for loop

# iterates over every element in object

# for loop : str
name = "Walter White"

for char in name:
    print(char) # new line

for letter in name:
    print(letter,end=",") # same line


# for loop : list
palette = ["\nred","green","yellow",'white']

for color in palette:
    print(color)

for color in palette:
    print(color)
    for i in color:
        print(i)


# range()
for j in range(10): # stop 10-1
    print(j)

for k in range(4,8): # start 4 ; stop 8-1
    print(k)

for x in range(2,17,3): # start 2 ; stop 17-1 ; step = increment 3
    print("x:",x)