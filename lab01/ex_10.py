# 반환 값이 바로 int로 변환
first = int(input("첫 번째 숫자를 입력해 주세요: "))
second = int(input("두 번째 숫자를 입력해 주세요: "))

print(type(first), type(second))
print(f"두 수의 합: {first + second}")
print(f"두 수의 차: {first - second}")
print(f"두 수의 곱: {first * second}")
print(f"두 수의 비: {first / second}")