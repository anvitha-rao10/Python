result, count = [], 1
s = input("Enter a string: ")
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result.append(s[i - 1])
        if count > 1:
            result.append(str(count))
        count = 1
result.append(s[-1])
if count > 1:
    result.append(str(count))
print("Compressed String:", ''.join(result))
