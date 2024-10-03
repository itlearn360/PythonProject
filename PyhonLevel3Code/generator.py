# Generator function to generate Fibonacci sequence
def fibonacci_sequence(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Update values to next Fibonacci numbers
        count += 1

# Create a generator for the first 10 Fibonacci numbers
fib_gen = fibonacci_sequence(10)

# Iterate through the generator to get Fibonacci numbers
for number in fib_gen:
    print(number)
