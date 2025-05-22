# list data type
# ordered collection of elements
# array

l = [3,6,9]
# = [0,1,2] index

print(l)
print(type(l))
print(l[2]) # 9
# print(l[3]) # IndexError: list index out of range


# different data type element
l1 = [1,'one',1.0,False]
print(l1) # valid but not recmd.

# negetive indexing
l2 = ["a","b","c","d","e"]
#  = [-5,-4,-3,-2,-1]
print(l2[-3]) # c

# checking if element is present or not
if "b" in l2:
    print(True)
else :
    print(False)

# slicing & jump index
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(nums[1:12:4]) # 2,4,10
# slice [1:12] ; jump by 3 index


