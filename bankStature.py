class BankAccount:
    
    def __init__(self):
        print("Welcome to your Account!!")
        self.balance = 1000
    def deposit(self, x):
        print("Your account has been credited by ",x)
        self.balance = self.balance + x
    def withdraw(self,x):    
        print("Your account has been debiited by ",x)
        self.balance = self.balance - x
    def __printBalance(self):
        print(self.balance)
    def getter(self):
        self.__printBalance()
a1 = BankAccount()
a1.deposit(500)
a1.withdraw(1000)
# a1.__printBalance()
a1.getter()