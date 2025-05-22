# seek() , tell() & truncate()

sk = open('file2.txt','r')

# seek()
sk.seek(14)
print(sk.read())
# whr to begin from

sk2 = open('file2.txt','r+')
# tell()
print(sk2.tell()) # 0 : at [0]

sk2.read(6)
print(sk2.tell()) # 6 : at [6] ; we read 6 chars

sk2.seek(20)
print(sk2.tell()) # 20 : at [20] ; seek count

sk2.read()
print(sk2.tell()) # 34 : at [34] ; read all [34]
# tells whr are we in file (int) ; seek count

# truncate()
sk2.truncate(15)
sk2.seek(0)
print(sk2.read())
# resize file to 15 bytes

sk.close()




