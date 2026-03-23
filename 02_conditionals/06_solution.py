# 6. Transportation Mode Selection
# Choose a mode of transportation based on the distance (e.g., <3km : Walk, 3-15 km: Bike, >15km: Car).

distance = 5

if distance < 3:
    transportation = "Walk"
elif distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"

print("AI recommends you transport of:",transportation)