# Task 3: Product Pricing (Dictionaries)

# 1. Create dictionary
price_dict = {
    "Laptop": 65000,
    "Mouse": 700,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000,
    "Speaker": 2500
}

print("Original Dictionary:")
print(price_dict)

# 2(a). Add new product
price_dict["Webcam"] = 3500

print("\nAfter Adding Webcam:")
print(price_dict)

# 2(b). Update price
price_dict["Mouse"] = 850

print("\nAfter Updating Mouse Price:")
print(price_dict)

# 2(c). Remove product

product = "Printer"

if product in price_dict:
    del price_dict[product]
    print("\nPrinter removed successfully.")
else:
    print("\nProduct not found.")

print(price_dict)

# 3. Average Price

total = sum(price_dict.values())
average = total / len(price_dict)

print("\nAverage Price:", average)

# Extra

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("\nMost Expensive Product:")
print(max_product, price_dict[max_product])

print("\nLeast Expensive Product:")
print(min_product, price_dict[min_product])