# i = 0
# while i < 10:
# 		print(i)
# 		i += 1
		
# 		if i == 5:
# 				print('break')
# 				break


# 실습 문제 18번
num = int(input("숫자를 입력하세요: "))

if num <= 0:
    print("음수는 안 됩니다.")
else:
    count = 0
    #print(f"while 이전: num = {num}, count = {count}")
    while num > 0:
        print('현재 숫자: ', num)
        count += 1
        num -= 1
        #print(f"while 이후: num = {num}, count = {count}")
    
    print(f"반복 횟수: {count}번")