import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # 인자로 받은 함수 실행
        result = func(*args, **kwargs)  # 전달 받은 걸 다 넘김
        end_time = time.time()

        print(f"실행시간: {end_time - start_time:.10f}")

        return result   
    return wrapper  # 내부 함수의 리턴값과 시작, 끝 시간 print까지 얻게 됨


# fibonacci_dp = timing_decorator(fibonacci_dp)
@timing_decorator
def fibonacci_dp(n):
    if n == 0:
        return [0]
    
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
        # n까지 감

    return fib


def fibonacci_gen(n):
    a, b = 0, 1
    #print(f"a: {a}, b: {b}")
    for _ in range(n+1):
        yield a
        a, b = b, a+b
        #print(f"a: {a}, b: {b}")

@timing_decorator
def fibonacci_deco(n):
    return [ _ for _ in fibonacci_gen(n)]


fibonacci_dp(4000)
fibonacci_deco(4000)