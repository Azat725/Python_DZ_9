def delete_numbers(array = [1, 2, 3, 4, 5, 5, 6, 6, 7, 5, 2, 10], delete_number = 5):
    list_of_delete_numbers = []
    
    for i in array:
        if i == delete_number:
            list_of_delete_numbers.append(delete_number)
    
    return len(list_of_delete_numbers)

print(delete_numbers())