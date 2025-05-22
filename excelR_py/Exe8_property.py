# @property

class Bank:
    def __init__(self,name,acc,balance):
        self.name = name
        self.acc = acc
        self.__balance=balance
    
    @property
    def balance(self):
        return f'Bal. : {self.__balance}'
    
    @balance.setter
    def balance(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f'{amount} credited to acc:{self.acc}')
        elif amount<0 :
            if self.__balance<abs(amount):
                print("Insuffecient Balance")
            else :
                self.__balance+=amount
                print(f'{abs(amount)} debited from acc:{self.acc}')
        

b = Bank("Abc",380091,45300)
print(b.balance)

b.balance = -5000   # -15000, -50000
print(b.balance)