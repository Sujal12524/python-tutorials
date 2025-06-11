# Learning string operation in Python

# Concentration
first = "Sujal"
last = "Bhandari"
full = first + " " + last
print("Full Name:", full)

# Srting Formatting (f-strings)
age = 20
print(f"My name is {first} and I am {age} years old.")

# String Methods
message = " Hello, Python!  "
print("Original:", message)
print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Stripped:", message.strip())
print("Replaced:", message.replace("Python", "World"))

# Slicing
word = "programming"
print("First 5 letters:", word[:5])
print("Last 3 letters:", word[-3:])
print("Middle part:", word[3:8])
