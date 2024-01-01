def count_letters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)


string_test = 'Today is My Best Day'
count_letters(string_test)
