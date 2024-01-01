def get_user_info(name, age, *args, email=None, **kwargs):
    print("User Information:")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    if args:
        print("Additional Positional Arguments:", args)
    if kwargs:
        print("Additional Keyword Arguments:", kwargs)


user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_email = input("Enter your email: ")
get_user_info(user_name, user_age, "AdditionalArg1", "AdditionalArg2", email=user_email, city="palava", country="india")
