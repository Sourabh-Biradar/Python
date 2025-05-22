# old formatting
# str.format()

# 1
info = "{} wears {} and plays for {}"
player = "Virat"
jersey = 18
team = "RCB"

p_info = info.format(player,jersey,team)
print(p_info)

# 2
person = "{1} works at {0}" # order
name = "Abc"
company = "BMW"

per_info = person.format(company,name)
print(per_info)