inputPW = input("패스워드 입력: ")
PW = 'abc'

for i in range(5):
    if inputPW != PW:
        print("패스워드가 틀렸습니다.")
        print(f"기회 {5-i}번 남았습니다.")
        inputPW = input("패스워드 입력: ")
    else:
        print("로그인 성공!")
        break
else:
    print("기회 소진. 로그인 잠금")