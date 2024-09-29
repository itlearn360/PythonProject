from abc import ABC, abstractmethod

# Abstract class (Base class)
class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass  # Abstract method, no implementation here

# Concrete class for SavingsAccount
class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.04  # 4% interest rate for savings account

# Concrete class for CurrentAccount
class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.02  # 2% interest rate for current account

# Function to display interest of any account
def display_interest(account):
    print(f"Interest for the account is: {account.calculate_interest()}")

# Create objects for each account type
savings = SavingsAccount(1000)
current = CurrentAccount(1000)

# Display the interest for each account
display_interest(savings)   # Output: Interest for the account is: 40.0
display_interest(current)   # Output: Interest for the account is: 20.0
