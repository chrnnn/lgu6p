def avg(nums):
    total = 0
    for x_k in nums:
        if type(x_k) == int:
            total += x_k
        else:
            print("숫자만 입력하세요.")
            break
    result = total / (len(nums))
    return result

X = [[78, 80, 95, 55, 67, 43], [45, 67, 90, 87, 88, 93]]

# 함수를 사용해 반환값을 표현
L = [round(avg(i),3) for i in X]
print(L)