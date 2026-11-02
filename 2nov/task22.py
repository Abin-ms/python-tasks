
# Parent Class
class Bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


# Child Class 1 - Deposit
class Deposit(Bank):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")


# Child Class 2 - Withdraw
class Withdraw(Bank):
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")


# Child Class 3 - Check Balance
class CheckBalance(Bank):
    def check_balance(self):
        print("Available Balance: ₹", self.balance)


# Child Class 4 - Display Account Details
class DisplayAccountDetails(Bank):
    def display_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.balance)


# Creating objects
deposit_obj = Deposit("Abin", 123456, 5000)
withdraw_obj = Withdraw("Abin", 123456, 5000)
balance_obj = CheckBalance("Abin", 123456, 5000)
details_obj = DisplayAccountDetails("Abin", 123456, 5000)


# Main Menu
while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit_obj.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw_obj.withdraw(amount)

    elif choice == 3:
        balance_obj.check_balance()


    elif choice == 4:
        details_obj.display_details()

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
