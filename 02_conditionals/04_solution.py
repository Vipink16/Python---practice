fruit = "Banana"
color = "Brown"

if fruit != "Banana":
    print("Check the fruit name again")
    exit()

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")