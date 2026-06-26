def modulo(a, b):
    """두 수를 나누어 나머지를 반환하는 함수이다.

    Args:
        a (int): 나눠지는 수
        b (int): 나누는 수

    Raises:
        ValueError: b가 0인 경우

    Returns:
        a를 b로 나눈 나머지
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없음")
    return a % b
