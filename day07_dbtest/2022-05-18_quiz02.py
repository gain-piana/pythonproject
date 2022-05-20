import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
name = input('2.사원의 이름의 일부를 입력받아서 검색해서 출력. >>> ')
cursor.execute("select * from emp where ename like '%" + '%s' % name.upper() + "%'")
a = []
for item in cursor:
    aa = item
    print(aa)
    a.append(list(aa))
# print(a)

conn.close()
