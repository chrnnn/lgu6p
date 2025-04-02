def dummy():
    print("I am a dummy function.")


def add(a, b):
    c = a + b
    return c

c = add(1, 2)
print(c)


###########################################
# 기본 인자
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet('홍길동', '안녕')
greet('홍길동')