import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
job = input('1.emp 테이블에 job을 입력받아 해당 job인 사원을 출력하세요. >>> ')
cursor.execute("select * from emp where job = '%s'" % job.upper())
a = []
for item in cursor:
    aa = item
    print(aa)
    a.append(list(aa))
# print(a)

conn.close()
