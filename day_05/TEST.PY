fruitlist=[]
fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 10},
            {'name': '포도', 'price': 4000, 'cnt': 20},
            {'name': '수박', 'price': 10000, 'cnt': 5}]

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 입력
    S - 판매
    C - 재고리스트
    D - 고객 정보 삭제 #수정필요
    ''').upper()  

    if choice=="I":  
        fruit = {'name': '', 'price': 0, 'cnt': 0} #체크
        while True:
            while True:
                fruit['name'] = input('이름 >>> ')
                if fruit['name'].isalpha():
                    break
                else:
                    print('이름을 정확하게 입력하세요.')
            check = 0
            for i in fruitlist:
                if i['name'] == fruit['name']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 이름이 있습니다.')

        while True:
            fruit['price'] = input('가격 >>> ')
            if fruit['price'].isdecimal():
                break

        while True:
            fruit['cnt'] = input('수량 >>> ')
            if fruit['cnt'].isdecimal():
                break
            
        fruitlist.append(fruit)
        page = len(fruitlist)-1
        print(fruitlist)


    elif choice=="C": 
        if page < 0:
            page += 1
            print('입력된 정보가 없습니다.')
        else:    
            print(f'현재 페이지는 {page+1}페이지 입니다.')
            print(custlist[page])

    elif choice == 'P':
        if page <= 0:
            print('첫번째 페이지 입니다.')
        else:    
            page -= 1
            print(custlist[page])
        print(f'현재 페이지는 {page+1}페이지 입니다.')

    elif choice == 'N':
        if page >= len(custlist)-1:
            print('마지막 페이지 입니다.')
        else:    
            page += 1
            print(custlist[page])
        print(f'현재 페이지는 {page+1}페이지 입니다.')
        
    elif choice == 'D':
        print(fruitlist)
        choice1 =input('삭제하려는 과일 이름을 입력하세요. >>> ')
        delok = 0
        for i in range(len(fruitlist)):
            if fruitlist[i]['name'] == choice1:
                print(f"{fruitlist[i]['name']}의 과일이 삭제되었습니다.")
                del fruitlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 과일정보 입니다.')
        print(fruitlist)
                
    elif choice == "U": 
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
            
    elif choice == "Q":
        print('프로그램을 종료합니다.')
        break