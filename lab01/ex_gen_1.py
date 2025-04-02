def get_number_generator(n):
    for i in range(n):
        print("before yield")
        yield i   # 0 반환하고 대기
        print("after yield")

# number = get_number_generator(3)
# print(next(number, 'end'))
# print()

# print(next(number, 'end'))  # after, before 출력, 1 반환
# print()

# print(next(number, 'end'))
# print()

# g = get_number_generator(10)

# for i in g:
#     print(i)


# 무한 숫자 생성기
def inf_number_generator():
    i = 1
    while True:
        yield i    # 1 반환 후 대기
        i += 1

num = inf_number_generator()
print(next(num))
print(next(num))