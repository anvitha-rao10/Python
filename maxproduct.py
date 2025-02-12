def max_product(arr):
    arr.sort()
    max_product = max(arr[0] * arr[1], arr[-1] * arr[-2])
    return max_product
input_str = input("Enter the array elements separated by spaces: ")
arr = []
for num in input_str.split():
    arr.append(int(num))
result = max_product(arr)
print("Maximum product:", result)
