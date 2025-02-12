def gcd(n1, n2):
    while n2:
        n1, n2=n2, n1%n2
    return n1
n3=int(input("Enter n1: ")) 
n4=int(input("Enter n2: "))
print(gcd(n3,n4)) 