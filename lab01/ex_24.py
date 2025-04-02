inputPW = input("패스워드 입력: ")
PW = "abc"

# while inputPW != PW:
#     print("패스워드가 틀렸습니다.")
#     inputPW = input("패스워드 입력: ")
#     if inputPW == PW:
#         print("로그인 성공!")
#     else:
#         print("다시 입력")

while True:
    inputPW = input("패스워드 입력: ")

    if PW == inputPW:
        print("로그인 성공")
        break
    else:
        print("다시 입력")

while PW != input("PW: "):
    print("다시 입력하세요.")
else: 
    print("로그인 성공")