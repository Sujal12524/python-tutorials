# Controlling loops with break and continue

# BREAK example: stop loop when number is found
print("Break example:")
for num in range(1, 10):
    if num == 5:
        print("Found 5, stopping.")
        break
    print("Current number:", num)

# CONTINUE example: skip even numbers
print("\nContinue example:")
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print("Odd number:", num)

# WHILE loop with break
print("\nWhile loop with break:")
i = 0
while True:
    if i == 3:
        break
    print("i =", i)
    i += 1