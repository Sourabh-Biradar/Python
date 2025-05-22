# Exercise 1
# Basic Calculator

print("Enter a number :")

num1 = int(input()) 

print("Enter another number :")

num2 = int(input()) 

add = num1 + num2 # addition
sub = num1 - num2 # substraction
mul = num1 * num2 # multiplication
div = num1 / num2 # division
mod = num1 % num2 # modulus : reminder

intDiv = num1 // num2 
# floor or integer division : omits decimals

exp = num1 ** num2 
# exponential : num1 ^ num2

print(add,sub,mul,div,mod,intDiv,exp)
