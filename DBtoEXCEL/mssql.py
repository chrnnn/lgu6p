############
# 실행 파일 - mssql
from db2excel import DB2EXCEL

# 클래스 인스턴스 생성
db2excel = DB2EXCEL()

# MSSQL 연결 후 쿼리 실행
data = db2excel.query_mssql(
    server="localhost",   # 또는 IP주소
    user="chrin-test",         # SQL Server 계정
    password="1234",      # 계정 비밀번호
    database="lily_book", # 사용할 데이터베이스
    query="SELECT * FROM customer"  # 실제 테이블명으로 수정
)

# 결과 엑셀로 저장```
db2excel.export_to_excel(data, "test_output.xlsx")
