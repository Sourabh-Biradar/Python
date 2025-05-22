# list comprehenstion

l = [i for i in range(8)]
print(l) # [0, 1, 2, 3, 4, 5, 6, 7]

la = [x+x for x in range(5)]
print(la) # [0, 2, 4, 6, 8]

lb = [j+3 for j in range(5)]
print(lb) # [3, 4, 5, 6, 7]

ls = [3,6,9,12,15]
lc = [i*i for i in ls if i%2==1] 
print(lc) # [9, 81, 225]

# i*i from list `ls` only `if thy are odd prints`