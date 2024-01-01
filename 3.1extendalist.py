
original_list = [1, 2, 3]

# i. By using + operator
new_list1 = original_list + [4, 5, 6]

# ii. By using Append()
new_list2 = original_list.copy()  
new_list2.append(4)
new_list2.append(5)
new_list2.append(6)

# iii. By using extend()
new_list3 = original_list.copy()  
new_list3.extend([4, 5, 6])

# Displaying the results
print("Original List:", original_list)
print("Extended List using + operator:", new_list1)
print("Extended List using Append():", new_list2)
print("Extended List using extend():", new_list3)
