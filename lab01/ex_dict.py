d = {
    'foo': 'foo@naver.com',
    'var': 'var@gmail.com',
    'egg': 'egg@kakao.com'
}
print(d)
print(d['foo'])

# 값 지우기
del d['foo']
print(d)

# 새로운 값 추가하기
d['foo'] = 'foo@naver.com'
print(d)

# 기존값 업데이트
d['foo'] = 'foo@kdt.co.kr'
print(d)

# 리스트, 숫자, 문자, 딕셔너리 다 넣을 수 있음
d['list'] = [1,2,3,4,5]
print(d)

# 키 조회
print(d.keys())

for key in d.keys():       # for key in d와 똑같음
    print(key) # 키
    print(d[key]) # 값

# 값 반복하기
for value in d.values():
    print(value)

# 키, 값 둘다 반복
for k, v in d.items():
    print(k, v)

# 키 없음을 방지하는 방법
print( d.get('bar', None) ) # 있으면 가져오고, 없으면 None
if d.get('bar', None) == None:
    print('조회하신 키가 없습니다.')
else:
    # 키를 이용한 작업...
    pass

# default로 없는 키를 조회하면 0을 반환
# 만약 괄호 안에 list 적었다면 []을 반환
from collections import defaultdict
dd = defaultdict(int)
print(dd)
print(dd['a'])

dd = defaultdict(list)
print(dd)
print(dd['a'])