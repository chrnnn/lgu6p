# 다른 자료형을 담고 있는 리스트
# L = [1, 'foo', True, 3.14, (1, 2)]
# t = L[4]

# print(t[1])
# # 또는
# print(L[4][1])


# # 중첩 리스트
# #      0 1 2
# L2 = [[1,2,3],   # 0번
#       [4,5,6]]   # 1번

# print(L2[0][2])


# 행렬 표현
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []

for row in A:  # 1~ 4~ 7~
      B = []
      for col in row:  #1,2,3
            B.append(col * 2)
      result.append(B)
print(result)    
