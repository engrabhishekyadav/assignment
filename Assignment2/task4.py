# Task 4: Loop Control

daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily_sales:

    if sale == -1:

        print("Corrupted Data Found")
        break

    elif sale == 0:

        print("No Sales Today")
        continue

    else:

        total_sales = total_sales + sale

        print("Running Total :", total_sales)

print("Final Total Sales :", total_sales)