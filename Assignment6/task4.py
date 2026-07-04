# Task 4: File Reader with Exception Handling

file = None

try:
    filename = input("Enter filename: ")
    file = open(filename, "r")

    print("First three lines:")
    for line_number in range(3):
        line = file.readline()

        if line == "":
            break

        print(line, end="")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    if file:
        file.close()

    print("File operation attempted.")
