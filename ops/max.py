def max(a, b):
    """_summary_

    Args:
        a (_type_): int | float | None
        b (_type_): int | float | None

    Raises:
        ValueError: int | float | None
    Returns:
        _type_: int | float | None
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a if a > b else b
