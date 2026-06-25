def root(a, b):
    """a의 b제곱근을 반환합니다.

    Args:
        a (int | float): 제곱근을 구할 수
        b (int | float): 몇 제곱근인지

    Returns:
        int | float: a의 b제곱근 값
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "숫자로 쳐주세요"
    return a ** (1 / b)