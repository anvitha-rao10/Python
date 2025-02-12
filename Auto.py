import math
x=float(input("Enter x: "))
if x>1.5:
    sum=35+((math.ceil(x-1.5))*25)
    print(sum)
else:
    print(35)    