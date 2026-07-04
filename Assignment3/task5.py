# Task 5: filter()

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda x: x > 500, prices))

less_equal_500 = list(filter(lambda x: x <= 500, prices))

print("Greater than 500")
print(greater_than_500)

print("Less than or equal to 500")
print(less_equal_500)