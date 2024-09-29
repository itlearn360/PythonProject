# Global variable
total_balance = 10000  # Total balance of the bank


# Function to simulate a user's bank account
def user_account():
    # Local variable
    user_balance = 1000  # Each user starts with $1000

    # Function to deposit money to user's account
    def deposit(amount):
        nonlocal user_balance  # Refers to the local user_balance
        user_balance += amount
        print(f"${amount} deposited to user account. User balance: ${user_balance}")

    # Function to withdraw money from user's account
    def withdraw(amount):
        nonlocal user_balance  # Refers to the local user_balance
        if amount <= user_balance:
            user_balance -= amount
            print(f"${amount} withdrawn from user account. User balance: ${user_balance}")
        else:
            print("Insufficient funds in user account.")

    # Return the inner functions
    return deposit, withdraw


# Accessing the global balance
def add_to_total_balance(amount):
    global total_balance  # Refers to the global total_balance
    total_balance += amount
    print(f"Total bank balance updated: ${total_balance}")


# Create a user account and access deposit/withdraw functions
deposit, withdraw = user_account()

# Deposit and withdraw money in the user account (local variables)
deposit(200)  # Output: $200 deposited to user account. User balance: $1200
withdraw(150)  # Output: $150 withdrawn from user account. User balance: $1050

# Access the global total balance
add_to_total_balance(500)  # Output: Total bank balance updated: $10500
