def rev(n):
    num = 0
    while n > 0:
        last = n % 10  
        num = num * 10 + last 
        n = n // 10  
    return num
num = int(input("Enter a number: "))
print(f"The reversed number is: {rev(num)}")  
