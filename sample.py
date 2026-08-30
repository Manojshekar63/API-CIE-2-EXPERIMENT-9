"""
Sample Python code with intentional bugs for AutoFixAI testing.
"""


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Bugs:
    - Allows negative prices
    - Allows discount greater than 100%
    - Does not validate input types
    """
    discount = price * discount_percent / 100
    return price - discount


def find_maximum(numbers):
    """
    Find the maximum number in a list.

    Bugs:
    - Crashes when the list is empty
    - Does not validate input type
    """
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def is_valid_email(email):
    """
    Check whether an email address is valid.

    Bugs:
    - Does not handle None
    - Incorrectly accepts strings without a domain
    - Does not validate input type
    """
    return "@" in email


def calculate_average(numbers):
    """
    Calculate the average of numbers.

    Bugs:
    - Division by zero for an empty list
    - Does not validate input type
    """
    return sum(numbers) / len(numbers)


def remove_duplicates(items):
    """
    Remove duplicate elements from a list.

    Bugs:
    - Does not preserve the original order
    - Fails with certain unhashable elements
    """
    return list(set(items))


def get_user_name(users, user_id):
    """
    Find a user's name by ID.

    Bugs:
    - Crashes if the user does not exist
    - Assumes every user has an 'id' and 'name'
    """
    for user in users:
        if user["id"] == user_id:
            return user["name"]

    raise Exception("User not found")


def fibonacci(n):
    """
    Generate the nth Fibonacci number.

    Bugs:
    - Incorrect handling of n = 0
    - Negative values are not handled
    - Recursive implementation becomes inefficient for large n
    """
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def calculate_total(items):
    """
    Calculate the total price of items.

    Bugs:
    - Assumes every item contains 'price'
    - Does not validate price values
    - Does not handle None
    """
    total = 0

    for item in items:
        total += item["price"]

    return total
