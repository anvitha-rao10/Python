def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s=input("Enter a word or sentence: ")
print(reverse(s))