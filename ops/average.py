def average(numbers):
    """숫자 리스트의 평균을 반환하는 함수이다.

    Args:
        numbers (list): 평균을 구할 숫자 리스트

    Raises:
        ValueError: 리스트가 비어있는 경우

    Returns:
        numbers의 평균값
    """
    if not numbers:
        raise ValueError("빈 리스트는 평균을 구할 수 없음")
    return sum(numbers) / len(numbers)
