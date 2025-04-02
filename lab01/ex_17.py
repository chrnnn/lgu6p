# a = -3
# if a > 0:
# 		print("postive")
# elif a < 0:
# 		print("negative")
# else:
# 		print("zero")
         
                
# 17번 실습 문제
height = float(input("키를 입력해 주세요(m): "))
weight = float(input("몸무게를 입력해 주세요(kg): "))
bmi = round(weight / height**2)

# if bmi >= 25:
#     print("비만입니다.", "BMI:", bmi)
# elif 25 > bmi and  bmi >= 23:
#     print("과체중입니다.", "BMI:", bmi)
# elif 23 > bmi and  bmi >= 18.5:
#     print("정상입니다.", "BMI:", bmi)
# else: 
#     print("저체중입니다.", "BMI:", bmi)


if bmi >= 25:
    print("비만입니다.", "BMI:", bmi)
elif bmi >= 23:
    print("과체중입니다.", "BMI:", bmi)
elif bmi >= 18.5:
    print("정상입니다.", "BMI:", bmi)
else:
    print("저체중입니다.", "BMI:", bmi)