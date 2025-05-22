# file handling
# file I/O

# open() , read() & write()
f = open('textfile.txt','r') # file_name , READ mode
f = open('textfile.txt') # READ mode default
print(f)


# 'r' = read only mode
print(f.read()) # all content
print(f.read(5)) # read jst STARTING `5` bytes

# trying write in read only mode
# print(f.write(":)")) # io.UnsupportedOperation: not writable


# 'w' = write only mode
# DELETES existing content & writes
g = open('textfile.txt','w')
gw = g.write("oops :(") 
print(gw) # how many chars written

h = open('file2.txt','w')
hw = h.write("file 2 content ...")
print(hw) # how many chars written
# CREATES file2.txt & Writes in it


# 'a' = append mode
# writes at EoF
i = open('file2.txt','a')
ia=i.write('appended in text')
print(ia)


# 'x' = create mode
# creates file if doesnt exist
j = open('file3.txt','x')


# 't' = text
# used for text files ; default
# 'rt' 'wt' 'at' 'xt' ...
k = open('file3.txt','t')

# 'b' = binary (image / audio file)
# 'rb' 'wb' 'ab' 'xb' ...
l = open('file2.txt','rb')
print(l.read()) # b''


# close()
# ALWAYS close files
f.close()
g.close()
h.close()
i.close()
j.close()
k.close()
l.close()