"""
Sample Python code with one intentional bug for AutoFixAI testing.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Bug:
    - Crashes with ZeroDivisionError when the list is empty.
    """
    if not numbers:
        return None  # or handle it as needed
    return sum(numbers) / len(numbers)

def count_words(sentence):
    """
    Count the number of words in a given sentence.

    Bug:
    - Raises TypeError if the input is not a string.
    - Raises ValueError if the sentence is empty.
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    if not sentence:
        raise ValueError("Sentence cannot be empty.")
    return len(sentence.split())

def get_element(items, index):
    """
    Retrieve an element from a list using an index.

    Bug:
    - Raises TypeError if the items are not a list.
    - Raises IndexError if the index is out of range.
    """
    if not isinstance(items, list):
        raise TypeError("Items must be a list.")
    if index < -len(items) or index >= len(items):
        raise IndexError("Index out of range.")
    return items[index]

def apply_discount(price, discount):
    """
    Apply a discount to a price.

    Bug:
    - Raises TypeError if the price or discount is not a number.
    - Raises ValueError if the discount is out of range (0-100).
    """
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number.")
    if not isinstance(discount, (int, float)):
        raise TypeError("Discount must be a number.")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    return price * (1 - discount / 100)

def calculate_root(operand, root):
    """
    Calculate the nth root of a number.

    Bug:
    - Raises TypeError if the operand or root is not a number.
    - Raises ValueError if the root is less than or equal to zero.
    """
    if not isinstance(operand, (int, float)):
        raise TypeError("Operand must be a number.")
    if not isinstance(root, (int, float)):
        raise TypeError("Root must be a number.")
    if root <= 0:
        raise ValueError("Root must be greater than zero.")
    return operand ** (1 / root)