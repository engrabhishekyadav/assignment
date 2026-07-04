# Task 2: Categories (Sets)

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Office",
    "Audio"
]

# 1. Create a set
categories_set = set(categories)

print("Unique Categories:")
print(categories_set)

# 2. Add a new category
categories_set.add("Gaming")

# Add duplicate category
categories_set.add("Electronics")

print("\nAfter Adding Categories:")
print(categories_set)

# 3. Check if category exists
print("\nDoes 'Office' exist?")
print("Office" in categories_set)

# Extra
print("\nTotal Unique Categories:")
print(len(categories_set))