# matchcase statement

# switch statement
# NOTE : ONLY first true case is executed ; `_` for default case

color = "Red"

match color:
    case "Blue":
        print("its blue")
    case "Red":
        print("its Red")
    case _:
        print("its not a color!!")


match color:
    case "maroon":
        print("its maroon") 
    case _ if color=="red": 
        print("its RED") 
    case _ if color != "Black":
        print("its not black")
       
