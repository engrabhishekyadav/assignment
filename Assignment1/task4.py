# Task 4: Combined Operations

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Office",
    "Audio"
]

price_dict = {
    "Laptop": 65000,
    "Mouse": 700,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000,
    "Speaker": 2500
}

# 1. Create catalog list

catalog = []

for i in range(len(products)):
    product = products[i]
    price = price_dict[product]
    category = categories[i]
    catalog.append((product, price, category))

print("Catalog:")
for item in catalog:
    print(item)

# 2. Create category_to_products dictionary

category_to_products = {}

for i in range(len(products)):
    category = categories[i]
    product = products[i]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("\nCategory to Products:")
print(category_to_products)

# 3. Category with maximum products

max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("\nCategory with Maximum Products:")
print(max_category)

print("Products:")
for product in category_to_products[max_category]:
    print(product)