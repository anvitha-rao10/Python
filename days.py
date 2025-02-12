import math
x = int(input("Enter seconds: "))
days = x //(24 * 60 * 60)
sec = x % (24 * 60 * 60)
hours = sec //(60 * 60)
sec =sec % (60 * 60)
minutes = sec //60
seconds = sec % 60
print(days, hours,  minutes,  seconds)