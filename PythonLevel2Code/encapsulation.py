class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute, hidden from direct access

    # Public method to view the balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

# Create a BankAccount object
account = BankAccount("12345", 1000)

# Accessing the balance using a getter method
print("Current Balance:", account.get_balance())  # Output: Current Balance: 1000

# Depositing money
account.deposit(500)  # Output: $500 deposited successfully.
print("New Balance:", account.get_balance())  # Output: New Balance: 1500

# Withdrawing money
account.withdraw(200)  # Output: $200 withdrawn successfully.
print("New Balance:", account.get_balance())  # Output: New Balance: 1300

# Attempting to directly access the private balance (will cause an error)
# print(account.__balance)  # This will raise an AttributeError
