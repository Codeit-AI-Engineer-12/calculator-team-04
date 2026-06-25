def multiply(a, b):
    # TODO: 두 수를 곱해 반환하세요.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a * b
