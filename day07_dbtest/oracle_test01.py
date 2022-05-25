#pip install cx_oracle ← 이걸 cmd든 터미널이든 실행해서 설치해야 아래 코드가 돌아감.
#오라클 db와 연동을 위한 라이브러리 설치
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp where deptno = 10")

for item in cursor:
    print(item[1], item[5])

conn.close()
