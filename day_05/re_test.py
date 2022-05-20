# import re

# # a = 'hello, world!'

# # # match는 무조건 첫글자부터 찾는다. 따라서 처음부터 안나오면 NONE이 나오게됨.
# # print(re.match('hello',a))
# # print(re.match('python',a))
# # print(re.match('world',a))

# # print(re.search('hello',a))
# # print(re.search('^world!',a))
# # print(re.search('world!$',a))

# # str1 = '123 hello HELLO'
# # print(re.match('[0-9]+', str1))
# # print(re.match('[0-9]*', str1))
# # print(re.search('[0-9]', str1))

# # print(re.match('a*b','b'))
# # print(re.match('a*b','aaaab'))
# # print(re.match('a+b','b'))
# # print(re.match('a+b','aaaab'))
# # print(re.match('a+b','aaaa'))

# # print(re.match('abc.d', 'abaas'))
# # print(re.match('ab.d', 'abxd'))

# # print(re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}','0200-1111-1111'))

# p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
# print(p.search('s7tup@gmail.com'))
# a=''
# while not p.search(a):
#     a = input('첫글자는 영어소문자,두번째부터 @전까지 4글자이상이고 영어소문자,숫자,_가능. @와.사이에 영어소문자자로 3글자이상이고, .뒤에 2글자이상 영어소문자 >>> ')
# print(a + '정상적으로 입력됨.')

import re

def customer_input(custlist):
    customer = {'name': '', 'gender': '', 'email': '', 'birthyear': ''}
    customer['name'] = input('이름 >>> ')
    while True:
        customer['gender'] = input('성별(M,F) >>> ').upper()
        if customer['gender'] in ('M','F'):
            break
    
    while True:
        p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
        customer['email']=''
        while not p.search(customer['email']):
            customer['email'] = input('email >>> ')
        check = 0
        for i in custlist:
            if i['email'] == customer['email']:
                check = 1
                break
        if check == 0:
            break
        print('중복되는 이메일이 있습니다.')
    
    while True:
        customer['birthyear'] = input('생년월일(4자리) >>> ')
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal():
            break
    
    custlist.append(customer)
    page = len(custlist)-1
    print(custlist)
    
    return page


def customer_c(custlist, page):
    if page < 0:
            page += 1
            print('입력된 정보가 없습니다.')
    else:    
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        print(custlist[page])

    return page

def customer_p(custlist, page):
    if page <= 0:
            print('첫번째 페이지 입니다.')
    else:    
        page -= 1
        print(custlist[page])
    print(f'현재 페이지는 {page+1}페이지 입니다.')

    return page


def customer_n(custlist, page):
    if page >= len(custlist)-1:
            print('마지막 페이지 입니다.')
    else:    
        page += 1
        print(custlist[page])
    print(f'현재 페이지는 {page+1}페이지 입니다.')

    return page 

def customer_delete(custlist, page):
    print(custlist)
    choice1 =input('삭제하려는 이메일 주소를 입력하세요. >>> ')
    delok = 0
    for i in range(len(custlist)):
        if custlist[i]['email'] == choice1:
            print(f"{custlist[i]['name']}님의 정보가 삭제되었습니다.") #같은 따옴표를 두 번 쓸수는 없으므로.
            if page == len(custlist)-1:
                page -= 1
            del custlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 고객정보 입니다.')
    print(custlist)
    
    return page
    
def customer_update(custlist):
    while True:
        print(custlist)
        choice1 =input('수정하려는 이메일 주소를 입력하세요. >>> ')
        idx = -1
        for i in range(len(custlist)):
            if custlist[i]['email'] == choice1:
                idx = i
                break
        if idx == -1:
            print('등록되지 않은 고객정보 입니다.')
            break
        
        choice2 = input('''
----------------------------------------
다음 중 수정할 항목을 선택하세요(종료:exit)
- name, gender, birthyear 중 입력
----------------------------------------
항목 >>> ''')
        if choice2 in ('name','gender','birthyear'): ###몰랐던 부분
            custlist[idx][choice2] = input(f'수정할 {choice2}를 입력하세요. >>>')
            print(custlist[idx])
            break
        
        elif choice2 == 'exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break



