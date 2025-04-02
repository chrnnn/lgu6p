# with open( "file_w.txt", "a", encoding="utf-8" ) as f:
#     f.write( 'Hello Python!\n' )
#     f.write( '안녕 파이썬' )

# with open( "file_w.txt", "r", encoding="utf-8" ) as f:
#     lines = f.readlines()
#     print(lines, type(lines))   # 리스트 반환
#     for line in lines:
#         print(line, end='') # 파일 한 줄씩 읽고 출력, 줄바꿈 막음


# 실습 문제 48번
import os
import ex_45
input_files = os.listdir('./data')

with open( "ex_48.txt", "w" ) as fw:
    for file in input_files:
        if 'txt' == file[-3:]:
            with open( f"./data/{file}", "r", encoding="utf-8" ) as f:
                lines = f.readlines()   # 리스트 형태
                name = file[:-4]
                nums = [float(line.strip()) for line in lines]
                # print(nums)
                m = ex_45.mean(nums)
                s = ex_45.std(nums)
                fw.write(f"{name:>8}: {m:.2f}, {s:.2f}\n")