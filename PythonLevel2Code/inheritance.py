# Parent class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name        # common attribute for all employees
        self.age = age          # common attribute for all employees
        self.salary = salary    # common attribute for all employees

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# Child class Manager (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)  # Call the constructor of the parent class
        self.department = department         # Unique attribute for Manager

    def manage_team(self):
        print(f"{self.name} manages the {self.department} department.")

# Child class Developer (inherits from Employee)
class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)  # Call the constructor of the parent class
        self.programming_language = programming_language  # Unique attribute for Developer

    def write_code(self):
        print(f"{self.name} writes code in {self.programming_language}.")

# Create a Manager object
manager1 = Manager("Alice", 45, 90000, "Sales")
manager1.display_details()      # Display common details
manager1.manage_team()          # Display Manager specific method

# Create a Developer object
developer1 = Developer("Bob", 30, 70000, "Python")
developer1.display_details()    # Display common details
developer1.write_code()         # Display Developer specific method
