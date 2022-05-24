import cx_Oracle
conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
sql="SELECT * FROM TEST"
cursor.execute(sql)
rs=cursor.fetchall()
cursor.close()
conn.commit()
conn.close()
for i in range(len(rs)):
    print(rs[i])

sellfruit = input("어떤 과일을 판매하시겠습니까?")
sellcnt = input("몇개를 판매하시겠습니까?")
for i in range(len(rs[i])):
    if rs[i][0] == sellfruit:
        sellcnt1 = rs[i][2]-int(sellcnt)
conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("update test set cnt = '{0}' where NAME = '{1}'".format(sellcnt1,sellfruit))
cursor.close()
conn.commit()
conn.close()