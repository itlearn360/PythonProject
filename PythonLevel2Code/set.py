# Step 1: List of email addresses with potential duplicates
email_list = [
    "example1@mail.com", "example2@mail.com", "example1@mail.com",
    "example3@mail.com", "example2@mail.com", "example4@mail.com"
]

# Step 2: Convert the list to a set to remove duplicates
unique_emails = set(email_list)

# Step 3: Print the unique email addresses
print("Unique email addresses for the campaign:")
for email in unique_emails:
    print(email)
