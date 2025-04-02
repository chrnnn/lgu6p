def mean(nums):
    total = 0
    for x_k in nums:
        if type(x_k) == int:
            total += x_k
        else:
            print("숫자만 입력하세요.")
            break
    result = total / (len(nums))
    return result

L1 = [10, 20, 30, 'ㅎ']
print(mean(L1))

# 또는 sum()함수 사용하기 ~