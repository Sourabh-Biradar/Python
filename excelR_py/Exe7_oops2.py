# Exercise 7 : OOPS
# ATM 

class Bank:
    def __init__(self,name,acc,balance):
        self.name = name
        self.acc = acc
        self.__balance=balance
    
    def get_balance(self):
        return f'Bal. : {self.__balance}'
    
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
            return f'{amount} credited to acc:{self.acc}'
        elif amount<0 :
            if self.__balance<abs(amount):
                return "Insuffecient Balance"
            else :
                self.__balance+=amount
                return f'{abs(amount)} debited from acc:{self.acc}'
        

b = Bank("Abc",380091,45300.8)
print(b.get_balance())

print(b.set_balance(30000))   # -15000, -50000
print(b.get_balance())

