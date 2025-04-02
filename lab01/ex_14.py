r = float(input("반지름 입력: "))
pi = 3.14
area = pi * r**2
circum = 2 * pi * r
d = r * 2

print(f"반지름이 {r}인 원의 면적은 {round(area, 2)}입니다.")
print(f"이 원의 둘레는 {circum:.2f}입니다.")
print(f"이 원의 지름은 {d}입니다.")