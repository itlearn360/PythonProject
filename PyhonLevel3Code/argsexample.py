def log_message(level, *messages, **details):
    print(f"Log Level: {level}")

    # Handling positional arguments (*args)
    print("Messages:")
    for message in messages:
        print(f"- {message}")

    # Handling keyword arguments (**kwargs)
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


# Example of logging an INFO level message with multiple messages and details
log_message("INFO", "System running", "No issues detected", user="Admin", timestamp="2024-10-03")

# Example of logging an ERROR level message with only one message and additional details
log_message("ERROR", "File not found", file_path="/var/logs/error.log", user="Admin")
