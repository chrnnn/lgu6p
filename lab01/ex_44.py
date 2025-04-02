operations = {
'+': lambda x, y: x + y,
'-': lambda x, y: x - y,
'*': lambda x, y: x * y,
'/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
}

x = float(input("첫 번째 숫자를 입력하세요: "))
y = float(input("두 번째 숫자를 입력하세요: "))
func = input("연산자를 입력하세요 (+, -, *, /): ")
if func in operations:
    result = operations[func](x, y)
    print(f"{x} {func} {y} = {result}")
else:
    print("올바른 연산이 아닙니다.")