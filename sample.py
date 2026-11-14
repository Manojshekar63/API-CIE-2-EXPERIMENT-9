def check_even(num):
    """
    Determines if a number is even or odd.

    Parameters:
    num (int): The number to check.

    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.

    Raises:
    TypeError: If the input is not an integer.
    ValueError: If the input is not a valid integer.
    """
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")
    
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test cases
print(check_even(4))  # Should return "Even"
print(check_even(5))  # Should return "Odd"
print(check_even(0))  # Should return "Even"
print(check_even(-4)) # Should return "Even"
print(check_even(-5)) # Should return "Odd"