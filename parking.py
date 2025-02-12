def max_sequence(arr):
    max_count = 0  
    current_count = 0  
    for slot in arr:
        if slot == 'S':
            current_count += 1 
        else:
            max_count = max(max_count, current_count)  
            current_count = 0  
    max_count = max(max_count, current_count)
    return max_count
input_str = input("Enter the parking lot slots : ")
arr = input_str.split()
result = max_sequence(arr)
print("Maximum number of cars: ", result)
