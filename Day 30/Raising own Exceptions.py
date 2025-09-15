height = float(input("Height: "))
weight = int(input("Weight" ))
if height > 3:
    raise ValueError("Human Height shoule not be over 3 metres.")
bmi = weight / height**2
print(bmi)