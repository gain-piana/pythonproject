#pip install cx_oracle ← 이걸 cmd든 터미널이든 실행해서 설치해야 아래 코드가 돌아감.
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("drop table test")
cursor.execute("create table test(id number(2))")
cursor.execute("insert into test values(01)")
cursor.close()
conn.commit()
conn.close()