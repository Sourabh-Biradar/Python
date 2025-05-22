# str slicing []
t = "Iron-Man"

# len(t) = 8

print(t[0:3]) # index 0 to 2 : Iro

print(t[5:7]) # index 5 to 7 : Ma

print(t[2:]) # on-Man

print(t[:6]) # Iron-M

print(t[:]) # index : 0 to 7

# negetive indexing 

print(t[0:-6]) # Ir
# [0:len(t)-6] = [0 : 8-6] = [0:2] 

print(t[-2:-5]) # nothing

print(t[-5:-2]) # n-M