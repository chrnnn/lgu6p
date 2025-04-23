############
# 실행 파일 - mysql
from db2excel import DB2EXCEL

# 객체 생성
db2excel = DB2EXCEL()


# MySQL에서 데이터 가져오기
data = db2excel.query_mssql(
    host="127.0.0.1",
    user="chrin-test",
    password="1234",
    database="lily_book",
    query="SELECT * FROM customer"  # 실제 테이블 이름
)

# 엑셀로 저장
db2excel.to_excel(data, filename="output.xlsx")
