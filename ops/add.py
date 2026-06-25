def add(a: int | float, b: int | float):
    # TODO: 두 수를 더해 반환하세요.
    """_summary_
    숫자가 아닌 값이 입력으로 들어오면 None을 반환합니다.
    Args:
        a (_type_): int | float
        b (_type_): int | float

    Returns:
        _type_: int | float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "메롱"
    return a + b
