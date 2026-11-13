def add_numbers(a, b):
    """
    Adds two numbers a and b.

    Parameters:
    a (int or float): The first number to add.
    b (int or float): The second number to add.

    Returns:
    int or float: The sum of a and b.

    Raises:
    TypeError: If either a or b is not a number.
    ValueError: If a or b is out of a reasonable range (e.g., negative numbers).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Both a and b must be numbers.")
    if not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers.")
    
    result = a + b
    return result

# Test the function with different inputs
print(add_numbers(10, 5))  # Expected output: 15
print(add_numbers(3.5, 2.5))  # Expected output: 6.0
print(add_numbers(0, 0))  # Expected output: 0

# Edge case: negative numbers
print(add_numbers(-10, 5))  # Expected output: -5

# Edge case: non-numeric input
try:
    print(add_numbers("10", 5))
except TypeError as e:
    print(e)  # Expected output: Both a and b must be numbers.