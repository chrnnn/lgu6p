# 리스트 안에 딕셔너리
data = [
    {'name':'철수', 'math':85, 'eng':90, 'sci':75},
    {'name':'준호', 'math':73, 'eng':85, 'sci':93},
    {'name':'영희', 'math':92, 'eng':88, 'sci':90}
]

# for d in data:
#     total = d['math'] + d['eng'] + d['sci']
#     avg = total/3


result = {}

for d in data:  # 한 사람 데이터
    total = 0
    for k, v in d.items():  # 키와 값 반복
        if k != 'name': # 키가 name이 아니면~
            total += v
    avg = total/(len(d)-1)  # 계산하고 result 사전에 넣기
    result[d['name']] = [total, round(avg,3)]
print(result)


# name = data.pop('name')
# print(data)
# for d in data:
#     for k, v in d.items():
#         total += v
#         ave = total/(len(d))
#         result[name] = [total, round(ave,3)]
# print(result)
                        