def extract_email_parts(email):
    username, domain = email.split('@')
    email_tuple = (username, domain)
    return email_tuple
user_email = input("Enter your email address: ")
result_tuple = extract_email_parts(user_email)
print("Username:", result_tuple[0])
print("Domain:", result_tuple[1])
