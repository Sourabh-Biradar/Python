# list methods

l = [11,10,7,8,9]

# list.append()
l.append(6)
print(l) # add `6` to end of list ; [11,10,7,8,9,6]

# list.sort()
l.sort()
print(l) # [6,7,8,9,10,11]

# list.sort(reverse=True)
l.sort(reverse=True)
print(l) # [11, 10, 9, 8, 7, 6]

# list.reverse()
l.reverse()
print(l) # [6,7,8,9,10,11]

# list.index()
print(l.index(9)) # 3
# returns index of element (frst occurence)
print(l.index(19)) # valueError
print(l.index(8,1,4)) # (ele,slice) ; (8 ,[1:4])
print(l.index('z',1,4)) # valueError

# list.count()
print(l.count(3)) # 0
# returns count of element

# list.copy()
nums = l 
print(nums)
nums[3]=99
print(l)
l[5] = 18
print(nums)
# nums is reference of l ,any changes to one ,applies for both

x = l.copy()
x[3] = 7
print(x)
print(l)
# since `x` is copy of `l` , changes to `x` won't affect `l`
# NOTE : changes to `l` affects `x`

# list.insert()
l.insert(3,-5) # index 3 value -5
print(l)
# index 3 value -5 , len extends , index 3 move up to 4 & so on

# list.extend()
m = ["a","b","c"]
x.extend(m)
print(x)
# extend `x` by adding `m` to it
# changes original list

# concat
k = l + m
print(k)

