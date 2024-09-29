# Create a dictionary to store student information
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A"},
}

# Accessing a student's information
print("Alice's information:", students["Alice"])  # Output: Alice's information: {'age': 20, 'grade': 'A'}

# Adding a new student
students["David"] = {"age": 23, "grade": "C"}
print("Updated students list:", students)

# Modifying a student's grade
students["Bob"]["grade"] = "A"
print("Bob's updated grade:", students["Bob"])

# Removing a student from the dictionary
del students["Charlie"]
print("Updated students list after removing Charlie:", students)

# Loop through the dictionary to display all student information
for student, info in students.items():
    print(f"{student}: Age {info['age']}, Grade {info['grade']}")
