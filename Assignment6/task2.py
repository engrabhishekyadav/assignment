# Task 2: Bill Calculator with Error Handling

prices = [120, 350, "abc", 500, -200, 800]
total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Price is not a number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total = total + price
        print("Added price:", price)
        print("Running total:", total)

    except TypeError as error:
        print("Skipped invalid item:", error)

    except ValueError as error:
        print("Skipped invalid item:", error)

print("Final total:", total)
