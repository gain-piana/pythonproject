name = input('2.사원의 이름의 일부를 입력받아서 검색해서 출력. >>> ')
print("select * from emp where job like '%" + '%s' % name.upper() + "%'")