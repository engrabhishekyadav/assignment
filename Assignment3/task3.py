# Task 3: Lambda Function

gst = lambda price: price + (price * 18 / 100)

print(gst(100))

# Extra

gst_discount = lambda price: (price + (price * 18 / 100)) * 0.90

print(gst_discount(100))