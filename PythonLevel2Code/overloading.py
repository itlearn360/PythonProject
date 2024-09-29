class Calculator:
    # Method to simulate overloading using default arguments
    def add(self, a, b, c=None):
        # If the third argument is not provided, add only two numbers
        if c is None:
            return a + b
        else:
            # If the third argument is provided, add all three numbers
            return a + b + c

# Create an object of the Calculator class
calc = Calculator()

# Call the 'add' method with two arguments
result1 = calc.add(5, 10)
print("Sum of two numbers:", result1)  # Output: Sum of two numbers: 15

# Call the 'add' method with three arguments
result2 = calc.add(5, 10, 15)
print("Sum of three numbers:", result2)  # Output: Sum of three numbers: 30
