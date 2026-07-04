import math_utils
from math_utils import square

import string_utils

import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package import flat_discount, apply_tax


print("Math Utility Functions")
print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(6))

print()
print("String Utility Functions")
sample_text = "python modules assignment"
print("Capitalized Words:", string_utils.capitalize_words(sample_text))
print("Reversed String:", string_utils.reverse_string(sample_text))
print("Word Count:", string_utils.word_count(sample_text))

print()
print("Shop Package Functions")
print("Discounted Price:", disc.apply_discount(1000, 10))
print("Flat Discount:", flat_discount(1000))
print("Total Bill:", calculate_total([100, 200, 300]))
print("Amount After Tax:", apply_tax(600))
