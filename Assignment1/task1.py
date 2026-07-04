# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list of at least 6 products
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

print("Original Product List:")
print(products)

# 2. Create a tuple (product_name, price, category)
sample_product = ("Laptop", 65000, "Electronics")

print("\nSample Product Tuple:")
print(sample_product)

# 3. Print the 2nd and last product
print("\nSecond Product:", products[1])
print("Last Product:", products[-1])

# 4. Append two new products
products.append("Webcam")
products.append("Headphones")

print("\nUpdated Product List:")
print(products)

# Extra (Optional)
product_list = list(sample_product)

# Change the price
product_list[1] = 70000

# Convert back to tuple
sample_product = tuple(product_list)