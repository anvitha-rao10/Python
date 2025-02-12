def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(f"The GCD of {n1} and {n2} is {gcd(n1, n2)}")
