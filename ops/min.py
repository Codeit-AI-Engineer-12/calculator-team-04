def min(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("숫자로 입력하세요")
    if a < b:
        return a
    else:
        return b
