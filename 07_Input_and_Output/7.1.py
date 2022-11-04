import math

diameter = float(input("Enter diameter: "))
length = float(input("Enter length: "))
X = math.pi * (diameter / 2.0) ** 2
C = math.pi * diameter
A = 2 * X + C * length
V = X * length
print("circumference is", C)
print("surface area is", A)
print("volume is", V)
