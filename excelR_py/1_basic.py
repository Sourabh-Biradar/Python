# 1 basics

a = 10
print ("a :",a)

# print()

b=2
c=4
print("*args :",a,b,c) # *args

print("sep :",a,b,c,sep="~") # sep = "~"

print("end :",a,b,end="-") # end = "-"
print(c)

# file
with open("1_output.txt","w") as f:
    print("file :",file=f)


print(a,b,c,flush=False) # flush