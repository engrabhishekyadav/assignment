# Task 5: Mini Program: Safe Shopping Cart

cart = []

while True:
    user_input = input("Enter price or q to quit: ")

    if user_input == "q":
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Negative price not allowed")

        cart.append(price)
        print("Price added:", price)

    except ValueError as error:
        print("Invalid price:", error)

total_bill = 0

for item in cart:
    total_bill = total_bill + item

print("Total items:", len(cart))
print("Total bill:", total_bill)
