# Task 6: Combined Utility Function

def process_prices(prices):

    discounted_prices = list(map(lambda x: x * 0.90, prices))

    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))

    return discounted_prices, filtered_prices


prices = [100, 500, 900, 50, 750]

discounted, filtered = process_prices(prices)

print("Discounted Prices")
print(discounted)

print("Filtered Prices")
print(filtered)