# lines

# readlines()
with open('file3.txt') as f:
    print(f.readlines())
# all lines in ONE LIST

# readline()
with open('file3.txt') as f:
    print(f.readline())
# reads one line & exits

# read all lines
with open('file3.txt') as f1:
    while True:
        line = f1.readline()
        if not line: # if line is empty (EoF)
            break
        print(line)

# writelines()
lines = ["\n43,88,12","\n32,89,95","\n92,97,100"]
with open('file3.txt','a') as f1:
    f1.writelines(lines)
# writes multiple lines 



