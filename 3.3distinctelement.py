def get_unique_elements(input_list):
 
    unique_list = list(set(input_list))
    return unique_list


original_list = [1, 2, 2, 3, 4, 4, 5,6,6,7,8,8]
result_list = get_unique_elements(original_list)

print("Original List:", original_list)
print("List with Distinct Elements:", result_list)
