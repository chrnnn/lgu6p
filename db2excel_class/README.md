# 프로젝트 개요
- 잠깐씩 사용

# 기능 명세서
- 해당 프로젝트 안에는 ~ 기능이 있음

## Main Functions
- MS-SQL, MySQL을 파이썬과 연동 및 쿼리 기능 지원 (클래스 구현)
    + DB2EXCEL 클래스
        - 연결 기능
        - 쿼리 실행 기능
        - 엑셀 내보내기 기능

- 웹 대시보드를 통해 간단히 테스트 (Streamlit 활용)
    + 포트번호 입력
    + 사용자 입력
    + 패스워드 입력

## 기대효과
- 웹 배포를 통해 어디에서도 쿼리 연습 가능

## 샘플 DB
- MS-SQL : https://
- MySQL : https://

# 사용법
- 셀프 테스트 방법
- 개발환경 조건 및 설치
    + 파이썬 3.13.2 버전 실행
    + 가상환경 설치
    + 라이브러리 실행
    + streamlit 웹 실행
```bash
$ git clone https://
$ virtualenv venv
$ source venv/Scrripts/activate  # Mac/Linux : source venv/lib/activate
(vemv) $ streamlit run app.py
```

## 향후 개선사항
- 한글 인코딩 문제 발생 (현재 버그 수정 중)