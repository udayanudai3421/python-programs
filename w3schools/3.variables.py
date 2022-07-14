x = 5  # x is of type int
x = "Vinoth"  # xis now of type str
y = "Udayan"
print(x)
print(y)

 # Type casting
x = str(5)    # x will be '5'
y = int("5")  # y will be 5
z = float(5)  # z will be 5.0

print(x)
print(y)
print(z)

# Get the Type

x = 5
y = "John"
print(type(x))
print(type(y))

print("---------------------------")

print(type(7))
print(type("Udayan"))
print(type(2.7))

# Single or Double Quotes? - String variables can be declared either by using single or double quotes

x = "John"
# is the same as
x = 'John'

# Case-Sensitive - Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a

# Assign Multiple Values - Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Global Variables 

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()   # Function calling