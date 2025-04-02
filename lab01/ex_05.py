a = 10
b = '이름'
c = 100

print(a)
print(b)
print(c)
print(a,b,c)

# 문자 사이 구분자 넣기
print(a,b,c, sep=';')

# 문자 사이 공백 없애기
print(a,b,c, sep='')


# end 옵션
print(a, end='')   # 줄바꿈 없앰
print(b)

print(a, end='\n')
print(b)