class BankAccount:
    def __init__(self,owner, balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit mus be positive.")

    def withdraw(self,amount):
        if 0<amount <=self.__balance:
            self.__balance-=amount
            print(f"Withdrawn:{amount}")

        else:
            print("Not enough balance or invalid amount.")
    
    def check_balance(self):
        print(f"Current Balance:{self.__balance}")

acc=BankAccount("Abid",5000)
acc.check_balance()
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()
# print(acc.__balance)