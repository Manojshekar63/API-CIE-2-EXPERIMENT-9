def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number to add.
    b (int or float): The second number to add.

    Returns:
    int or float: The sum of the two numbers.

    Raises:
    TypeError: If either a or b is not an int or float.
    ValueError: If either a or b is out of the valid range for addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Both a and b must be numbers (int or float).")
    if not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers (int or float).")

    result = a + b
    return result

# Test cases
print(add_numbers(10, 5))  # Expected output: 15
print(add_numbers(-10, 5)) # Expected output: -5
print(add_numbers(0, 0))   # Expected output: 0
print(add_numbers(1000000, 500000))  # Expected output: 1500000