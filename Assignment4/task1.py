# Task 1

sales = [1200, 450, 980, 1500, 3000]

# Write data
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

# Read and print
with open("sales_data.txt", "r") as file:
    print(file.read())
