def calculate_vehicles(V, W):
    FW = (W-2*V) // 2
    TW = V - FW
    return TW, FW
V = int(input("Enter the total number of vehicles: "))
W = int(input("Enter the total number of wheels: "))
TW, FW = calculate_vehicles(V, W)
print("TW: ", TW)
print("FW: ",FW)
