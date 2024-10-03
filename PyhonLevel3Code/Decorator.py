import time

# Decorator to log the execution time of a function
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record the end time
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example function that we want to time
@log_execution_time
def process_data(data):
    # Simulating data processing by sleeping for 2 seconds
    time.sleep(2)
    print("Data processed")
    return len(data)

# Call the function
data = [1, 2, 3, 4, 5]
process_data(data)
