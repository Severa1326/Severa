import math
print("This is a program made in Python to automatically calculate the roots of a second order polynomial")
a = float(input("Please insert the value of the coefficient of x^2: "))
b = float(input("Please insert the value of the coefficient of x^1: "))
c = float(input("Please insert the value of the coefficient of x^0: "))

pre_determinant = (b**2 - 4*a*c)
if pre_determinant < 0:
    print("We are sorry. The second order polynomial has complex roots.")
else:
    determinant = math.sqrt(pre_determinant)
    positive_result = (-b + determinant)/(2*a)
    negative_result = (-b - determinant)/(2*a)
    determinant_equals_zero = (-b)/(2*a)
    if determinant > 0:
        print(f"""
The second order polynomial has two possible roots:
X1 = {positive_result}
X2 = {negative_result}""")
    else:
        print(f"""
The second order polynomial has one possible root:
X = {determinant_equals_zero}""")
