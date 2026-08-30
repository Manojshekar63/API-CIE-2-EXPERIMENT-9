"""
Sample Python code with one intentional bug for AutoFixAI testing.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Bug:
    - Crashes with ZeroDivisionError when the list is empty.
    """
    return sum(numbers) / len(numbers)
