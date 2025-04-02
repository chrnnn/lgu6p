import math
# print(dir(math))

#math.sqrt(2)
# 또는
# from math import sqrt, sin
# sqrt(2)

##################################################

# 실습 문제 45번
def mean(l):
    total = 0
    for k in range(len(l)):
        x_k = l[k]
        total += x_k
    N = len(l)
    result = total / N
    return result


def std(l):
    m = mean(l)
    var = mean( [ (x_k - m)**2 for x_k in l ] )
    sigma = math.sqrt(var)
    return sigma

# 소스 코드가 메인 스크립트 파일로 작동이 될 때 main으로 자동 초기화
# 다른 파일에서 불러온다면 __name__이 아니라 작동 ㄴㄴ
if __name__ == '__main__':
    L = [1,2,3,4,5,6,7,8,9,10]
    print(std(L))