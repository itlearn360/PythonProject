# Parent class
class Employee:
    def __init__(self, name):
        self.name = name

    # General method that can be overridden
    def work(self):
        print(f"{self.name} is working as a general employee.")


# Child class Manager, which overrides the work method
class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")


# Child class Developer, which also overrides the work method
class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")


# Create objects of each class
general_employee = Employee("John")
manager = Manager("Alice")
developer = Developer("Bob")

# Call the work method for each object
general_employee.work()  # Output: John is working as a general employee.
manager.work()  # Output: Alice is managing the team.
developer.work()  # Output: Bob is writing code.
