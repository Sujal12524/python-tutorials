# Practice with nested loops

rows = int(input("Enter number of rows: "))

# 1. Right-angle triangle (stars)
print("\nRight-angle triangle:")
for i in range(1, rows + 1):
    print("*" *i)

# 2. Number triangle
print("\nNumber triangle:")
for i in range(1, rows + 1):
    for j in range(1, i +1):
        print(j, end="")
        print()

# 3. Inverted triangle
print("\nInverted triangle:")
for i in range(rows, 0, -1):
    print("*" *i)

# 4. Pyramid pattern
print("\nPyramid pattern:")
for i in range(1, rows + 1):
    print(" "* (rows - i) + "* " * i)