shoplist = ['apple', 'mango', 'carrot', 'banana']
print(shoplist)

########### 자주 쓰는 기능 #############


# 1. 특정 위치값 변경
shoplist[0] = 'melon'
print(shoplist)
# apple이 melon으로 바뀜

# 2. 마지막에 요소 추가
shoplist.append('lego')
print(shoplist)

# 3. 리스트나 시퀀스 추가
shoplist.extend(['소고기', '닭고기'])
print(shoplist)

shoplist + ['소고기', '닭고기']
print(shoplist)

# 4-1. 제거 remove(value)
shoplist.remove('소고기')
print(shoplist)

# 4-2. 제거 del idex
del shoplist[0]
print(shoplist)


# 5. index
i = shoplist.index('banana')
print(i)

# 6. 리스트 길이
print(len(shoplist))

# 7. 빈 리스트
L = []

# 정렬
L = [3, 5, 2, 1, 0, 4]
L.sort()
print(L) # 정렬된 상태로 L 그자체가 바로 바뀜

L = [3, 5, 2, 1, 0, 4]
L_sorted = sorted(L) # 다른 값에 정렬된 L을 넣고 싶을 때
print(L)

# 역순 정렬
L = [3, 5, 2, 1, 0, 4]
L.sort(reverse=True)
print(L)

L = [3, 5, 2, 1, 0, 4]
L_sorted = sorted(L, reverse=True)
print(L)