def max_guests(T, E, L):
    current_guests = 0
    max_guests = 0
    for i in range(T):
        current_guests += E[i] - L[i]
        max_guests = max(max_guests, current_guests)
    return max_guests
T = int(input("Enter the number of hours: "))
E = list(map(int, input("Enter the guests entering at each hour: ").split()))
L = list(map(int, input("Enter the guests leaving at each hour: ").split()))
print(max_guests(T, E, L))
