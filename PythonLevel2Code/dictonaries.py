# Creating a dictionary
student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing a value using a key
print(student_info["name"])  # Output: Alice

# Modifying a value
student_info["grade"] = "A+"

# Adding a new key-value pair
student_info["major"] = "Computer Science"

# Removing a key-value pair
del student_info["age"]

print(student_info)
