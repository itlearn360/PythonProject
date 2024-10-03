def divide_numbers():
    try:
        # Ask for user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Attempt to divide the numbers
        result = num1 / num2

    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: You cannot divide by zero!")

    except ValueError:
        # Handle non-numeric input error
        print("Error: Please enter valid numeric values!")

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

    else:
        # This block executes if no exception occurs
        print(f"Result: {num1} / {num2} = {result}")

    finally:
        # This block always executes, regardless of exceptions
        print("Thank you for using the division program.")


# Run the program
divide_numbers()
