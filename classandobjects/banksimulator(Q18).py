#  Q18. Constructor and Multiple Operations
# Create a class BankAccount with a constructor that accepts name and balance. Create methods to:
# Deposit money.
# Withdraw money, provided the balance is sufficient.
# Display the current balance.

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self):
        amount = int(input("Enter the amount to deposite:"))
        self.balance = self.balance + amount
        self.display_balance()
    def withdraw(self):
        amount = int(input("Enter the amount to withdraw : "))
        if(amount > self.balance):
            print("insufficient balance!!!!!")
        else:
            self.balance = self.balance - amount
        self.display_balance()
    def display_balance(self):
        print("Available balance is :",self.balance)

s1 = BankAccount("Abin",1000)
s1.display_balance()
print("Withdraw money")
s1.withdraw()
print("Deposite money")
s1.deposit()
s1.display_balance()
