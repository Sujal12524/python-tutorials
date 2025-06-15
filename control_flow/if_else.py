# Making decision with if, elif, else

age = int(input("Enter your age: "))

if age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 60:
    print("You're an adult.")
else:
    print("You're a senior.")

# Bonus: checking even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")