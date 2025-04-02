import random

class Linear:
    def __init__(self, in_feature, out_feature):
        # 무작위 리스트를 3개씩 만들어 3행 2열 w 생성
        self.in_feature = in_feature
        self.out_feature = out_feature

        self.weight = [] # in_feature행, out_feature열
        for i in range(in_feature): 
            row = []    # 3행 리스트 만들기
            for j in range(out_feature):
                w = random.random()
                row.append(w)   # 행 하나에 숫자 2개 추가
            self.weight.append(row) # 생성된 행을 최종 w에 추가
        print('w: ', self.weight)

        # 결과에 더할 b1, b2
        self.bias = []  # 2개 (out_feature)
        for k in range(out_feature):
            b = random.random()
            self.bias.append(b)
        print('b: ', self.bias)
    
    def matmul(self, A, B):
        # A, B를 행렬곱하여 결과행렬 C 반환
        row = len(A)    # A의 행 수
        col = len(B[0]) # B의 열 수
        C = []
        # C를 0으로 초기화 C = [[0,0], [0,0]]
        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(0)
                # n번째 행 한 줄 완성
            C.append(temp)
            # temp 리스트를 C에 추가. [0,0]
        
        for i in range(len(A)): # C의 행 번호 생성
            for j in range(len(B[0])):  # C의 열 번호
                for k in range(len(A[0])):
                    C[i][j] += (A[i][k] * B[k][j])
        return C

    def forward(self, x):
        # x 행렬곱 self.weight + self.bias
        Z = self.matmul(x, self.weight)
        for i in range(len(Z)):
            for j in range(len(self.bias)):
                Z[i][j] = Z[i][j] + self.bias[j]
        return Z

linear = Linear(3, 2)
x = [ [1,2,3],
      [4,5,6] ]  # 2행 3열

# 결과는 2행 2열이 나와야 함
print( linear.forward(x) )


################################################3
# 결과 확인용
import numpy as np

x_np = np.array(x)
W_np = np.array(linear.weight)
b_np = np.array(linear.bias)

y_np = np.dot(x_np, W_np) + b_np
print(y_np)