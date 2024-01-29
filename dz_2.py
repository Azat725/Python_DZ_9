def func(array):
    min_number_in_array = array[0]
    for i in array:
        if i < min_number_in_array:
            min_number_in_array = i
        
    return min_number_in_array

print(func([2, 2, 4, 6, 1, 7]))

