# Task 4: map()

prices = [100, 250, 400, 1200, 50]

gst = lambda price: price + (price * 18 / 100)

prices_with_gst = list(map(gst, prices))

print("Original Prices")
print(prices)

print("Prices After GST")
print(prices_with_gst)