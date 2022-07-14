# Int 
x = 1
y = 3243134
z = -3525134

print(type(x))
print(type(y))
print(type(z))

print("________")

# Float
x = 1.22
y = 3.2321
z = -4.8555

print(type(x))
print(type(y))
print(type(z))

x = 25e6
y = 12E4
z = -654.85e75

print(type(x))
print(type(y))
print(type(z))

# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)  # convert from int to float:

b = int(y)  # convert from float to int:

c = complex(x)#convert from int to complex:

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number
import random
print(random.randrange(1 , 10))