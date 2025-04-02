# 인덱싱
#    0  1  2  3  4  5  6  7
L = [1, 2, 3, 4, 5, 6, 7, 8]
#   -8 -7 -6 -5 -4 -3 -2 -1
print(L[3])

# 음수 인덱스도 가능 (뒤에서부터 ~)
print(L[-1])

# 슬라이싱
# [start:end:stride]
print(L[1:3:1])

# 모두 생략
print(L[::])

# start, stride 생략
print(L[:3])

# end, stride 생략
print(L[3:])

# start, end 생략
print(L[::2])

# 음수 인덱스를 사용한 슬라이싱
print(L[-3::])

print(L[-7:-4:1])

print(L[-2:-6:-1])
