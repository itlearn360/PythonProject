# List of tuples containing name and age
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20), ("David", 35)]

# Sort the list of people by age using a lambda function
sorted_people = sorted(people, key=lambda person: person[1])

# Print the sorted list
print(sorted_people)
