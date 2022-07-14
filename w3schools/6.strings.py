a = "hello"
print(a)

# Multiline strings 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are array
a = "Udayan"
print(a[0])

# Loopind through a string 
for x in "banana":
    print(x)

# String length
a = "Udayan"
print(len(a))

# Check string
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
  print("Yes, 'free' is present.")

# Check if not
print("expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Slicing strings
a = "Hello World"
print(a[2:5])

# Slice from the start
b = "Hello World"
print(b[:5])

# Slice To the End
c = "Hello World"
print(c[2:])

# Negative Indexing
d = "Hello World"
print(d[-5:-2])

# Upper Case
e = "Hello World"
print(e.upper())

# Lower case
f = "Udayan"
print(f.lower())

# Remove Whitespace
g = "  Udayan       "
print(g.strip())

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

