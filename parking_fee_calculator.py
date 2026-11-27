vehicle_type = input("Enter vehicle type: ")
hours = float(input("Enter parking duration in hours: "))

if vehicle_type == "Two-wheeler":
    rate = 20
elif vehicle_type == "Four-wheeler":
    rate = 50
elif vehicle_type == "Heavy vehicle":
    rate = 100

total_fee = rate * hours
print("Vehicle Type:", vehicle_type)
print("Parking Duration (hours):", hours)
print("Total Parking Fee: Rs.", total_fee)