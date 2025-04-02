import pandas as pd

df = pd.read_excel("./data/scores.xlsx")

# df를 90도 돌려서 딕셔너리 형태로 뽑아내기
df = df.T.to_dict()
data = [ v for k, v in df.items() ]
print(data)

result = {}
for d in data:  # 한 사람 데이터
    total = 0
    for k, v in d.items():  # 키와 값 반복
        if k != 'name': # 키가 name이 아니면~
            total += v
    avg = total/(len(d)-1)  # 계산하고 result 사전에 넣기
    result[d['name']] = [total, round(avg,3)]
print(result)