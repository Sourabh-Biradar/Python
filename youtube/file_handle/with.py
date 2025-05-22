# with keyword

# auto closes file

with open('file3.txt','w') as t:
    t.write('file 3 content')
    

with open('file3.txt') as t1:
    print(t1.read())
