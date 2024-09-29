class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = None  # Private attribute
        self.set_grade(grade)  # Using setter to initialize the grade
    
    # Getter method to access the private grade attribute
    def get_grade(self):
        return self.__grade
    
    # Setter method to set and validate the grade
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
            print(f"Grade updated to {self.__grade} for {self.name}.")
        else:
            print("Invalid grade! Grade must be between 0 and 100.")

# Create a Student object
student1 = Student("Alice", 85)

# Access the grade using the getter method
print("Current Grade:", student1.get_grade())  # Output: Current Grade: 85

# Attempt to set a valid grade using the setter method
student1.set_grade(92)  # Output: Grade updated to 92 for Alice.

# Attempt to set an invalid grade using the setter method
student1.set_grade(105)  # Output: Invalid grade! Grade must be between 0 and 100.

# Access the updated grade using the getter method
print("Updated Grade:", student1.get_grade())  # Output: Updated Grade: 92

