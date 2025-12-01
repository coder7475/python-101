class BankAccount:
    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    
# Usage
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1300