class Person:
    # 직접 호출하지 않아도 init 함수를 자동으로 호출
    def __init__(self, name, height, weight):
        # 변수 초기화 (self 안 붙이면 지역변수가 됨.. 에러)
        self.name = name
        self.height = height
        self.weight = weight

    def speed(self):     # 인자가 없음
        return (self.height / self.weight) * 5
    
    def print(self):
        print(f"나는 {self.name}이고 키{self.height}")

# 객체 생성
p1 = Person("Tom", 170, 100)  # 클래스로부터 유도되는 변수
print(type(p1))
print(p1.name)
print(p1.weight)
print(p1.height)

# 클래스를 만들면 클래스형 변수를 여러 개 쉽게 만들 수 있음
p2 = Person("Kim", 180, 85)

# 객체 내부 함수 실행. 대상체에 따라 결과가 달라짐
print(p1.speed())
print(p2.speed())