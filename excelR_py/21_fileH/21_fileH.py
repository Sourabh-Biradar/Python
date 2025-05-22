# File Handling
# open,read/write, close

# read
a = open("greet.txt",'r') 

print(a.read())

a.close()

# write
b = open("greet.txt",'w')
print(b.write("New content"))  # returns num of chars written
b.close()

# append
c = open("greet.txt",'a')
c.write("\n Hello! Greetings.")
c.close()

# creating new file
# seek,tell
d = open("new_f.txt","w")
d.write("Aaaaaa,Bbbbbbb,ccccccc")
print(d.tell())
d.seek(10)
d.write("zzzzz")
print(d)