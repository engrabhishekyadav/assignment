# Task 2

# read()

with open("sales_data.txt", "r") as file:
    data = file.read()

print("Using read()")
print(data)

# readline()

with open("sales_data.txt", "r") as file:
    first = file.readline()

print("Using readline()")
print(first)

# readlines()

with open("sales_data.txt", "r") as file:

    lines = file.readlines()

numbers = []

for line in lines:
    numbers.append(int(line.strip()))

print("Using readlines()")
print(numbers)