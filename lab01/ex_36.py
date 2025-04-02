# a = [1,2,3,4]
# b = [4,5,6,7]
# c = 0

# for i in range(len(a)):
#     c += a[i] * b[i]
# print(c)


A = [[1,0,1], [0,2,0], [1,2,1]]
B = [[2,3,1], [0,1,1], [1,1,1]]

# 결과 행렬 C 
row = len(A)    #A의 행 수
col = len(B[0]) #B의 열 수
C = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
        # n번째 행 한 줄 완성
    C.append(temp)
    # temp 리스트를 C에 추가

C = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        # 첫 번째 행렬의 열 개수 = 두 번째 행렬의 행 개수니까
        for k in range(len(A[0])):
            # i와 j는 바뀌지 않음
            C[i][j] += (A[i][k] * B[k][j])

print(C)