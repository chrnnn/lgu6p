import csv
import openpyxl
import pymssql
import mysql-connector-python
import pandas as pd


class DB2EXCEL:
    """
    데이터베이스에서 데이터를 가져와 엑셀 파일로 저장하는 클래스.
    
    지원 DB: MS-SQL, MySQL
    
    Example:
        db2excel = DB2EXCEL()
        data = db2excel.query_mssql(
            server="localhost", user="sa", password="1234", database="testdb", query="SELECT * FROM users"
        )
        db2excel.to_excel(data, filename="output.xlsx")
    """

    def query_mssql(self, server, user, password, database, query):
        """
        MSSQL 데이터베이스에서 데이터를 가져와 pandas DataFrame으로 반환하는 함수

        Parameters:
            server (str): MSSQL 서버 주소 (예: 'localhost' 또는 '127.0.0.1')
            user (str): MSSQL 사용자 이름
            password (str): MSSQL 비밀번호
            database (str): 사용할 데이터베이스 이름
            query (str): 실행할 SQL 쿼리

        Returns:
            pandas.DataFrame: 쿼리 결과
        """
        # MSSQL 서버와 연결
        conn = pymssql.connect(
            server=server,
            user=user,
            password=password,
            database=database
        )
        
        # 쿼리 실행하여 결과 가져오기
        df = pd.read_sql(query, conn)
        
        # 연결 종료
        conn.close()
        
        return df

    def query_mysql(self, host, user, password, database, query, port=3306):
        """
        MySQL에 접속해 쿼리 결과를 가져온다.
        """
        conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset='utf8mb4')
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        return [columns] + rows

    def export_to_excel(self, data, filename="output.xlsx"):
        """
        데이터를 엑셀 파일로 저장한다.
        1단계: 데이터를 CSV 형식으로 저장하고, 
        2단계: CSV 파일을 엑셀 파일로 변환한다.
        """
        
        # DataFrame인 경우
        if isinstance(data, pd.DataFrame):
            # 임시로 CSV 파일로 저장 (utf-8 인코딩)
            csv_filename = "temp_output.csv"
            data.to_csv(csv_filename, index=False, encoding='utf-8-sig')
            
            # CSV 파일을 엑셀로 변환
            wb = openpyxl.Workbook()
            ws = wb.active
            with open(csv_filename, newline='', encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                for row in reader:
                    ws.append(row)
            
            # 엑셀 파일 저장
            wb.save(filename)
            print(f"엑셀 파일로 저장됨: {filename}")

        # 리스트인 경우
        elif isinstance(data, list):
            wb = openpyxl.Workbook()
            ws = wb.active
            for row in data:
                ws.append(row)
            wb.save(filename)
            print(f"엑셀 파일로 저장됨: {filename}")
