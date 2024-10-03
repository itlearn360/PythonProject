# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to filter even numbers and square them
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

# Print the resulting list
print(squared_evens)  # Output: [4, 16, 36, 64, 100]
