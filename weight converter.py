weight = int(input("Weight: "))
flag = True
count = 0
while flag:
    unit = input("(L)bs or (K)g: ")
    unit = unit.upper()
    count += 1
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"You are {converted} kilos")
        break
    if unit.upper() == "K":
        converted = weight / 0.45
        print(f"Your are {converted} pounds")
        break
    else:
        print("Please input the right unit 'L' or 'K'. ")
        count += 1

print("Done")
