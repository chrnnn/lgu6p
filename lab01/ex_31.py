teams = ['타이거즈', '라이온즈', '트윈스', '베어스', '위즈',
         '랜더스', '자이언츠', '이글스', '다이노스즈', '히어로즈']

for team in teams:
    print(teams.index(team)+1, team)


# 리스트 안 갯수 알려줌
for i in range(len(teams)):
    print(f'{i+1}위 {teams[i]}')


# enumerate
for i, team in enumerate(teams):
    print(f'{i+1}위 {team}')