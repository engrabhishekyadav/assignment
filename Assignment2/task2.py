# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discount_count = 0

print("Order\tDiscount\tFinal Amount")

for order in orders:

    if order >= 2000:
        discount = order * 15 / 100

    elif order >= 1500:
        discount = order * 10 / 100

    elif order >= 1000:
        discount = order * 7 / 100

    else:
        discount = 0

    final_amount = order - discount

    print(order, "\t", discount, "\t\t", final_amount)

    total_revenue = total_revenue + final_amount

    if discount > 0:
        discount_count = discount_count + 1

print("\nTotal Revenue :", total_revenue)

# Extra
print("Orders with Discount :", discount_count)