def max(a, b):
    """두 수 중 더 큰 값을 반환합니다.

    Args:
        a (int | float): 비교할 첫 번째 숫자
        b (int | float): 비교할 두 번째 숫자

    Raises:
        ValueError: a 또는 b가 숫자(int, float)가 아닌 경우 발생

    Returns:
        int | float: a와 b 중 더 큰 값
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both a and b must be numbers.")
    return a if a > b else b
