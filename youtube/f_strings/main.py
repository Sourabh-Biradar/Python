# f-strings

# string formatting
# str = f"{var}"

country = "Spain"
continent = "Europe"
count = 4.78

atlas = f"{country} is in {continent} continent with {count:.1f} cr. population"
# {count:.1f} : rounds to `1` decimal point

print(atlas)

# single value
s = f"{2*7}"
print(type(s),s) # str

# read var name
value = 2*7
m = f"{{value}}"
print(m)



