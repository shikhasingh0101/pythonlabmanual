def create_cube_dict(start, end):
    cube_dict = {}
    for num in range(start, end + 1):
        if num % 2 != 0:  
            cube_dict[num] = num ** 3 
    return cube_dict


start_range = 1
end_range = 10
result_dict = create_cube_dict(start_range, end_range)

print("Dictionary of cubes for odd numbers in the range {}: {}".format((start_range, end_range), result_dict))
