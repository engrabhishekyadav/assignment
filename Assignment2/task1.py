# Task 1: Discount Rules

order = input("Enter order amount: ")

if order.isdigit():

    order = int(order)

    if order >= 2000:
        discount = order * 15 / 100

    elif order >= 1500:
        discount = order * 10 / 100

    elif order >= 1000:
        discount = order * 7 / 100

    else:
        discount = 0

    final_amount = order - discount

    print("Original Amount :", order)
    print("Discount :", discount)
    print("Final Amount :", final_amount)

    # Extra
    tax = final_amount * 5 / 100
    total = final_amount + tax

    print("Tax :", tax)
    print("Total Amount :", total)

else:
    print("Invalid Input")