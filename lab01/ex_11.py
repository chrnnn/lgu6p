height = float(input("키를 입력하세요(m): "))
weight = float(input("몸무게를 입력하세요(kg): "))

bmi = weight / (height**2)
print(f"당신의 bmi는 {bmi:.2f}입니다.")