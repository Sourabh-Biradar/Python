# Exercise 4 : File Handling

lines = [
    'Python is fun\n',
    'File handling is important\n',
    'Practice makes u perfrct\n'
]

# write
with open("notes.txt",'w') as f:
    for l in lines:
        f.write(l)
    f.close()

# append
with open("notes.txt",'a') as f:
    f.write("Keep learning everyday\n")
    f.close()

# read 
with open("notes.txt",'r') as f:
    for l in f:
        print(l.strip())
    f.close()