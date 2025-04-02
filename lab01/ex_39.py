# n = int(input("n: "))

# 1~n 리스트
# L = []
# for i in range(1, n+1):
#     L.append(i)

# print(L)


# 리스트 컴프리헨션
# 반환값을 어떻게 표현할지 맨 앞에 적음
# L = [ i*2 for i in range(1, n+1) ]

# ex_39
L = [ n for n in range(1,21) if n % 2 == 0]
print(L)