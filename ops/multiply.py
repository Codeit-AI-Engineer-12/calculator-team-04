def multiply(a, b):
    # TODO: 두 수를 곱해 반환하세요.
    """_summary_
    숫자가 아닌 값이 입력으로 들어오면 None을 반환합니다.

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: INT | FLOAT | None
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a * b
