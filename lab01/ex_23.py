inputID = input("아이디를 입력하세요: ")
ID = "chaerin"
PW = "1234"

if inputID == ID:
    inputPW = input("비밀번호를 입력하세요: ")
    if inputPW == PW:
        print("로그인 성공!")
    else: 
        print("비밀번호가 틀렸습니다.")
else:
    print("그런 아이디는 존재하지 않습니다.")
