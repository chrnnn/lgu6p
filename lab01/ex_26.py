menu = """[메뉴를 입력하세요]
1.게임시작      2.랭킹보기      3.게임종료 >>>"""
inputNum = input(menu)

while inputNum != 3:
    if inputNum == 1:
        print("->게임을 시작합니다.")
    else:
        print("->실시간 랭킹")
    inputNum = input(menu)
else:
    print("게임을 종료합니다.")