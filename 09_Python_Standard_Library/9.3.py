import math

# Test with 7 (3 bits), 8 (4 bits), 65,535 (16 bits), 65,536 (17 bits), and 4,294,967,295 (32 bits)
n = int(input("Enter a number: "))
bits_needed = math.floor(math.log2(n))+1
print("bits needed: ", bits_needed)
