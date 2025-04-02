# sub = ['국어', '수학', '영어']
# jisoo = [90, 85, 93]
# mansoo = [78, 92, 89]

# total = []
# for i in range(len(sub)):
#     total.append(jisoo[i] + mansoo[i])
#     print(f'{sub[i]} 총점 : {total[i]}')


# 중첩 개념 적용
scores = [ [90, 85, 93],
           [78, 92, 89] ]
# 지수의 수학 점수는?
print(scores[0][1])

print(len(scores[0]))
total_subjects = []
# 학생들의 각 과목 점수 총합
for sb in range(len(scores[0])): # 0, 1, 2
    total2 = 0
    for st in range(len(scores)): # 0, 1
        total2 += scores[st][sb]
    total_subjects.append(total2)
print(total_subjects)

# 각 학생들의 점수 총합
total_students = []
for st in range(len(scores)):
    total3 = 0
    for sb in range(len(scores[0])):
        total3 += scores[st][sb]
    total_students.append(total3)
print(total_students)


##################################################

# 
total_students = [0, 0]
total_subjects = [0, 0, 0]

for st in range(len(scores)):
    for sb in range(len(scores[0])):
        total_students[st] += scores[st][sb]
        # 한 학생의 점수들이 total_stu에 들어감
        total_subjects[sb] += scores[st][sb]

print(total_students)
print(total_students)