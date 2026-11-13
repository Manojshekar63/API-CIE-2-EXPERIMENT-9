
"""
Sample Python code with one intentional bug for AutoFixAI testing.
"""


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    if not numbers:
        return None
    return sum(numbers) / (len(numbers) - 1)
