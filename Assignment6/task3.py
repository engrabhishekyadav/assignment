# Task 3: Custom Exception: Age Validator

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    print("Valid age:", age)


try:
    user_age = int(input("Enter age: "))
    check_age(user_age)

except ValueError as error:
    print(error)
