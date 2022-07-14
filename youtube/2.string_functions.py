
# Variable
from math import *


name ="Virat Kohli"

# Function
uppercase_name = name.upper() 
check_name = uppercase_name.isupper()
print(f"Username is in uppercase?\n{check_name}")

print(len(name))

print(name[8])

print(name.index("h"))

print(name.replace("Virat", "Warner"))

print(33)

height = 6.2    # float or double (Decimal Point)

## Arithmetic Operators
print(3 + 3)

print(4.2 * 3 + 7)     # Operator Precedence

print(4.2 * (3 + 7))

print(6 % 5)   # Modulo or Modulus Operator

print(6 / 5)

num = 6
print(num)
print(str(num))   # Type casting (from int to string)

print(str(num) +" is greater than 3")   # String Concatenation

num = -6
print(abs(num))   # Absolute

power = 5   # 5^2
print(pow(power, 2))   # Power

print(max(2, 6)) # Maximum

print(f"Minimum Number: {min(3, 10)}") # Minimum

# Round
print(round(3.4))
print(round(3.6))

print(sqrt(3.6))

# Round down
print(floor(4.7))

# Round up
print(ceil(4.7))
