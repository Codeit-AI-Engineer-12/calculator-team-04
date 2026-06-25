def integer_division(a: int, b: int):
    """
    Perform integer division of two numbers.

    Parameters:
    a (int): The dividend.
    b (int): The divisor.

    Returns:
    int: The result of the integer division a // b.

    Raises:
    ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b
