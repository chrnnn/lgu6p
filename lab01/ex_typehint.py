def add(a, b):
    """
    두 수 a, b를 더하는 함수
    """
    return a+b

help(add)   # add(a, b)를 출력해줌


# 그냥 타입 알려주는 주석 같은 느낌..? 타입을 강제하진 않음
def mul(a: int, b: int) -> int:
    return a * b

print(mul(3, 4))
print(mul('3', 4))