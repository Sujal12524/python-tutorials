# using if else statements inside if statements

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "1234":
        print("Access granted.")
    else:
        print("Wrong password")
else:
    print("Unknown user.")

# Another example
marks = int (input("Enter your marks: "))

if marks >= 90:
    if marks == 100:
        print("Perfect score: ")
    else:
        print("Excellemt.")
elif marks >= 60:
    print("Good.")
else:
    print("Needs improvement.")