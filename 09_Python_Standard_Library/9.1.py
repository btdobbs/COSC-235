import math

# Test with 0, 45, 90, 180, and 225
theta = float(input("Enter \u03B8 in degrees: "))
radians = math.radians(theta)
sine = math.sin(theta)
cosine = math.cos(theta)
pythagorean_identity = sine*sine+cosine*cosine
print("\u03B8 in radians:", radians)
print("sin(\u03B8):", sine)
print("cos(\u03B8):", cosine)
print("Pythagorean Identity:", round(pythagorean_identity))
