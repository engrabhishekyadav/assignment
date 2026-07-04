# Task 5

with open("products.txt", "w") as file:

    for i in range(3):

        name = input("Enter Product Name: ")

        price = input("Enter Price: ")

        file.write(name + " | " + price + "\n")

print()

with open("products.txt", "r") as file:

    for line in file:

        print(line.strip())