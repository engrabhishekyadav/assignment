# Task 3: User Menu

orders = []

while True:

    print("\n1. Add Order")
    print("2. Show Orders")
    print("q. Quit")

    choice = input("Enter choice: ")

    if choice == "1":

        amount = input("Enter Order Amount: ")

        if amount.isdigit():

            orders.append(int(amount))

        else:
            print("Invalid Amount")
            continue

    elif choice == "2":

        total = 0

        if len(orders) == 0:
            print("No Orders Available")
            continue

        print("\nOrder\tDiscount\tFinal")

        for order in orders:

            if order >= 2000:
                discount = order * 15 / 100

            elif order >= 1500:
                discount = order * 10 / 100

            elif order >= 1000:
                discount = order * 7 / 100

            else:
                discount = 0

            final = order - discount

            total = total + final

            print(order, "\t", discount, "\t\t", final)

        print("Total :", total)

    elif choice == "q":

        print("Program Closed")
        break

    else:

        print("Invalid Choice")
        continue