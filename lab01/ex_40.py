def Qr(x, y):
    q = x // y
    r = x % y
    return (q, r)   # 반환 값이 2개면 튜플 사용

result = Qr(10, 3)
print(result)
print(result[0], result[1])


def Qr2(x, y):
    q = 0
    while x >= y:
        x -= y
        q += 1
    return(q, x)

result2 = Qr2(10, 3)
print(result2)


q = 0
r = 0
def Qr2(x, y):
    while True:
        x -= y
        if x > 0:
            q += 1
        elif x < 0:
            break
        else:
            q += 1

result2 = Qr2(10, 3)
print(result2)   