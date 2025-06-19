# Writing and using basic functions

# Define a simple function
def greet():
    print("Hello, Github! You're now using functions.")

# call the function
greet()

# Function with arguments
def add(a, b):
    result = a + b
    print("Sum is:", result)

add(5, 3)

# Function that returns a value
def square(x):
    return x * x

result = square(4)
print("Square of 4 is:", result)

# Function with user input
def welcome_user():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

welcome_user()