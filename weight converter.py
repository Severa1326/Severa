weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs?: ")
if unit.upper() == "L":
    transformed_weight = weight * 0.45
    print(f"You're {transformed_weight} {unit.upper()}")
elif unit.upper() == "K":
    transformed_weight = weight / 0.45
    print(f"You're {transformed_weight} {unit.upper()}")
else:
    print("Please select your weight in pounds (L) or kilograms (K)")

"done 03/03/2020"

