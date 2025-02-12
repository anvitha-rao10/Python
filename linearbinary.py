def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = list(map(int, input("Enter a list of numbers: ").split()))
target = int(input("Enter target number: "))
result_linear = linear_search(arr, target)
print(result_linear if result_linear != -1 else "Not found")
arr.sort()  
result_binary = binary_search(arr, target)
print(result_binary if result_binary != -1 else "Not found")
