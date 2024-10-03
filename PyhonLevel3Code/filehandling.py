import os


# Function to read student grades from a file
def read_student_grades(file_path):
    try:
        with open(file_path, 'r') as file:
            print("Current Student Grades:")
            content = file.readlines()
            if content:
                for line in content:
                    print(line.strip())
            else:
                print("No student records found.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


# Function to write a new student grade to the file
def write_student_grade(file_path, student_name, grade):
    try:
        with open(file_path, 'a') as file:  # Open in append mode to add a new record
            file.write(f"{student_name}: {grade}\n")
            print(f"Added record for {student_name} with grade {grade}.")
    except PermissionError:
        print(f"Error: You don't have permission to write to the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# Function to ensure the directory exists
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")
        except OSError as e:
            print(f"Error: Could not create directory '{directory}'. Reason: {e}")
    else:
        print(f"Directory '{directory}' already exists.")


# Main function to manage the file
def manage_student_grades():
    directory = "student_data"
    file_name = "grades.txt"
    file_path = os.path.join(directory, file_name)

    # Ensure the directory exists
    ensure_directory_exists(directory)

    # Read the current grades from the file
    read_student_grades(file_path)

    # Add a new student grade
    student_name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    # Write the new student grade to the file
    write_student_grade(file_path, student_name, grade)

    # Read the file again to confirm the addition
    read_student_grades(file_path)


# Run the program
manage_student_grades()
