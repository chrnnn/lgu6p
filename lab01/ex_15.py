e = 2.718
sqrt_2pi = 2.506

x = float(input("x를 입력: "))
mu = float(input("mu를 입력: "))
sigma = float(input("sigma를 입력: "))

fx = (1 / (sigma * sqrt_2pi)) * \
    e**(-(x-mu)**2 / (2 * sigma**2))
print(f"함숫값 f(x)는 {round(fx, 3)}입니다.")