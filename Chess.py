def horse(x1, x2, y1, y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    if (0<x2<7 and 0<y2<7):
        if (x==1 and y==2) or (x==2 and y==1):
            return "Valid"
        else:
            return "Invalid"
x1=int(input("Enter x1: "))
x2=int(input("Enter x2: "))
y1=int(input("Enter y1: "))
y2=int(input("Enter y2: "))
print(horse(x1, x2, y1, y2))