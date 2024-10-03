import re


# Function to validate email addresses
def validate_email(email):
    # Regular expression pattern for validating an email
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Use re.match() to check if the email matches the pattern
    if re.match(email_pattern, email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")


# List of emails to validate
emails = ["user@example.com", "invalid-email@", "john.doe@company.org", "admin@123", "hello.world@domain.com"]

# Validate each email in the list
for email in emails:
    validate_email(email)
