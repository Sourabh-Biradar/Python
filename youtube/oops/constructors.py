# OOPs

# constructors = default & parametrized
# spl. method in class used to create & init an obj
# __init__(self)
# gets called everytime a obj/instance is CREATED for tht class

class Player:
    def __init__(self,name,runs,wkts): # param constructor
        self.name = name
        self.runs = runs
        self.wkts = wkts
    def stats(self):
        print(f'Player {self.name} has scored {self.runs} & took {self.wkts} wkts')

player1 = Player('Abc',78,2)
player1.stats()

player2 = Player("Xyz",19,4)
player2.stats()