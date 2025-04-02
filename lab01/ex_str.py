# s = "Hello 'EASY' Python"
# print(s)

# s = "Hello, \n 'EASY' Python"
# print(s)

# # 명령어 환경에서는 그냥 type()만 해도 나오지만
# # 스크립트(소스) 파일에서는 print 해줘야 함
# t = type(s)
# print(t)

# # 형태를 갖는 문자열 사용 시, 따옴표 3개!
# s2 = """Hello, 
# "EASY" Python
# """
# print(s2)

# # f-string
# a = 10
# b = 20
# c = a * b
# print(f"{a} x {b} = {c}") 
# # 값이 찍히길 바라는 곳에 중괄호{}

# d = 5.2
# e = 21.234
# f = d * e
# #print("f:", f, "FAIL")
# print(f"{d:.1f} x {e:.1f} = {f:.1f}")

# g = "hello"
# print(f"{g:@^15}")

# lang = "python"
# ver = "3.10"
# print(lang+ver)
# print(lang * 3)

# # 타입이 다르면 error 발생
# print(lang * 3.2) 


s = "python,python"

# count()
print(s.count('p'))  # p가 1개 있으니 1이 나옴 

# find()
print(s.find('t'))  # 가장 앞에 있는 t의 인덱스값
                    # 없는 문자면 -1 반환

# replace()
print(s.replace('python', 'PYTHON'))
# 결과를 보여주는 것뿐. 문자열 s는 수정되지 x

# split()
print(s.split(','))  # ,를 기준으로 쪼개고 리스트로 반환
print(s.split())     # 기본값은 ' '

# join()
L = ['python', 'java', 'c++']
print( '::'.join(L) )  # ::로 연결

# strip()
s2 = "  python  \n\t"
print(s2.strip())  # 공백 없애줌
s3 = "@<python>!"
print(s3.strip('<>!'))

# isdigit(), isalpha(), isalnum()
s4 = "123"
print( s4.isdigit() )    # True
print( s4.isalpha() )    # False
print( s4.isalnum() )    # True

# upper(), lower()
s5 = 'PyThOn'
print( s5.upper() )
print( s5.lower() )