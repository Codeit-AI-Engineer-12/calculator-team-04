def min(a, b):
    """a와 b 중 작은 값을 반환한다.

    Args:
        a (int, float): 비교할 첫 번째 숫자
        b (int, float): 비교할 두 번째 숫자

    Raises:
        ValueError: a또는 b가 숫자가 아닐 때

    Returns:
        int, float: a와 b 중 더 작은 값
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("숫자로 입력하세요")
    if a < b:
        return a
    else:
        return b
