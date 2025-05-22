# for comperhension
# [exp. for x in sequence]

import pandas as pd

class Society:
    def __init__(self,name,flat):
        self.name=name
        self.flat=flat
    
    def info(self):
        print(f'owner : {self.name} ,flat no.: {self.flat}')


obj =[
    Society("Abc",201),
    Society("Xyz",908),
    Society("Mno",111)
]

# for comp
data = {
    "name":[e.name for e in obj],
    "flat":[e.flat for e in obj]
}      

df = pd.DataFrame(data)
print(df)