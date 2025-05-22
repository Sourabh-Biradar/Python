# Custom / user defined exception hanling

class AgeError(Exception):
    number = 21

try:
    num=int(input("Enter Age:"))
    if num < 21:
        raise AgeError
    else:
        print("Legal to drink")
except AgeError:
    print(f"{num} is NOT a legal age")
finally :
    print("Drinking is Injurious to health")

