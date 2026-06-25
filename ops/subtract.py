def subtract(a, b):
    """두 수의 차를 반환합니다.

    Args:
        a (int | float): 첫 번째 숫자
        b (int | float): 두 번째 숫자

    Returns:
        int | float: a에서 b를 뺀 값
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "숫자로 쳐주세요"
    return a - b

# 우엥 뭐가 뭔지 모르겠어영 우엥 