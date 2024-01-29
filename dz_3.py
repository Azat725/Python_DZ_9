def is_number_simple(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
        else:
            return True
        
        
def func(array = [7, 13, 29, 4, 15]):
    simple_numbers = []
    
    for i in array:
        if is_number_simple(number=i):
            simple_numbers.append(i)
    return len(simple_numbers)

print(func())