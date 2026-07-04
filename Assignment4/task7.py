# Task 7

prices = {

    "Mouse":500,

    "Keyboard":800,

    "Monitor":7000,

    "Pendrive":400,

    "Camera":5000

}

discount = float(input("Enter Discount Percentage: "))

total_discounted = 0

count = 0

with open("discount_report.txt","w") as file:

    file.write("Product | Original Price | Discounted Price\n")

    for product in prices:

        original = prices[product]

        discounted = original - (original * discount / 100)

        total_discounted = total_discounted + discounted

        count = count + 1

        file.write(product + " | " + str(original) + " | " + str(discounted) + "\n")

    average = total_discounted / count

    file.write("\n")

    file.write("Total Items: " + str(count) + "\n")

    file.write("Average Discounted Price: " + str(average))

with open("discount_report.txt","r") as file:

    print(file.read())