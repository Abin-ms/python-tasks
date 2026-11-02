
# PARENT CLASS
class Bank:

    def __init__(self, name, account_number, balance, pin):

        # Public attributes
        self.name = name
        self.account_number = account_number

        # Protected attribute
        self._bank_name = "ABC Bank"

        # Private attributes
        self.__balance = balance
        self.__pin = pin

    # Public method to access private balance
    def get_balance(self):
        return self.__balance

    # Public method to verify PIN
    def verify_pin(self, pin):
        return self.__pin == pin

    # Protected method to update balance
    def _update_balance(self, amount):
        self.__balance += amount


# CHILD CLASS 1 - DEPOSIT
class Deposit(Bank):

    def deposit(self, amount):

        if amount > 0:
            self._update_balance(amount)
            print(f"₹{amount} deposited successfully!")

        else:
            print("Invalid deposit amount!")


# CHILD CLASS 2 - WITHDRAW
class Withdraw(Bank):

    def withdraw(self, amount):

        pin = input("Enter your PIN: ")

        if not self.verify_pin(pin):
            print("Incorrect PIN!")

        elif amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.get_balance():
            print("Insufficient balance!")

        else:
            self._update_balance(-amount)
            print(f"₹{amount} withdrawn successfully!")


# CHILD CLASS 3 - CHECK BALANCE
class CheckBalance(Bank):

    def check_balance(self):

        pin = input("Enter your PIN: ")

        if self.verify_pin(pin):
            print("Available Balance: ₹", self.get_balance())

        else:
            print("Incorrect PIN!")


# CHILD CLASS 4 - DISPLAY ACCOUNT DETAILS
class DisplayAccountDetails(Bank):

    def display_details(self):

        print("\n------ ACCOUNT DETAILS ------")

        print("Bank Name:", self._bank_name)
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.get_balance())


# MULTIPLE INHERITANCE
class Account(Deposit, Withdraw, CheckBalance, DisplayAccountDetails):
    pass


# CREATING OBJECT
account = Account("Abin", 123456789, 5000, "1234")


# MAIN MENU
while True:

    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            account.display_details()

        elif choice == 5:
            print("Thank you for using ABC Bank!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")

