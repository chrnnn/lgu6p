def op (x, z, y):
    return(x+y)*z

x = 2
y = 3
z = 4

# 위치 인자
print( op(x, z, y) )
print( op(x, y, z) )    # 값이 다름!

# 키워드 인자
print( op(x=x, z=z, y=y) )

# 위치, 키워드 혼합 방식
print( op(x, y=y, z=z) )

# 혼합할 때 순서 잘못하면...
# print( op(y=y, x, z) )

# *args
def my_print(*args):
    print(args, type(args))
my_print('a', 'b', 'c')

# **kwargs
def my_print2(**kwargs):
    print(kwargs, type(kwargs))
my_print2(x = 'a', y = 'b', z = 'c')

#########################################

# 실습 문제 43번
def print_all(*args, **kwargs):
    print(args)
    print(kwargs)

# 각각 튜플과 딕셔너리 형태로 넘겨짐
print_all(1,2,3,4,5,6, x=100, y=300, z=400)