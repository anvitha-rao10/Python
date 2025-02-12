s = input("Enter a string: ")
hash_count = 0
result = []
for char in s:
    if char == '#':
        hash_count += 1  
    else:
        result.append(char) 
result = ['#'] * hash_count + result
print("Modified String:", ''.join(result))
