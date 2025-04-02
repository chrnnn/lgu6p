numbers = [10, 4, 5, -1, 6, 12, 40]

n = numbers[1::2]
total = 0
for i in n:
    total += i
print(total)

total = 0
for i in range(len(n)):
    total += n[i]
print(total)


# max 값 찾기
max_value = numbers[0]
for i in numbers[1:]:
    if i > max_value:
        max_value = i
print(max_value)