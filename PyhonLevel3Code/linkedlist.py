# Node class to represent each student in the LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # Data represents the student's name
        self.next = None  # The next pointer to the next node


# LinkedList class to manage the student list
class LinkedList:
    def __init__(self):
        self.head = None  # Head is the first node of the list

    # Method to add a student (node) at the end of the list
    def add_student(self, student_name):
        new_node = Node(student_name)  # Create a new node with the student's name
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as head
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Add the new node at the end
        print(f"Student {student_name} added to the enrollment list.")

    # Method to remove a student by name
    def remove_student(self, student_name):
        current = self.head
        previous = None
        while current and current.data != student_name:
            previous = current
            current = current.next

        if not current:  # If the student is not found
            print(f"Student {student_name} not found in the list.")
            return

        if not previous:  # If the student to remove is the head of the list
            self.head = current.next
        else:
            previous.next = current.next  # Remove the student by skipping the node

        print(f"Student {student_name} has been removed from the enrollment list.")

    # Method to display all students in the list
    def display_students(self):
        if not self.head:
            print("No students enrolled.")
            return

        current = self.head
        print("Enrolled students:")
        while current:
            print(f"- {current.data}")
            current = current.next


# Testing the LinkedList for student enrollment management

# Create a linked list object
enrollment_list = LinkedList()

# Adding students to the enrollment list
enrollment_list.add_student("Alice")
enrollment_list.add_student("Bob")
enrollment_list.add_student("Charlie")

# Display the current list of students
enrollment_list.display_students()

# Remove a student
enrollment_list.remove_student("Bob")

# Display the updated list of students
enrollment_list.display_students()

# Attempt to remove a student not in the list
enrollment_list.remove_student("David")
