fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 5},
          {'name': '포도', 'price': 4000, 'cnt': 20},
          {'name': '수박', 'price': 10000, 'cnt': 5}]

SUM=0
while True:
    choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        C - 재고리스트
        D - 삭제
        B - 매입
        Q - 종료
        ''').upper()

    if choice=="I":  
        fruit = {'name': '', 'price': 0, 'cnt': 0} #체크
        while True:
            while True:
                fruit['name'] = input('과일 이름 >>> ')
                if fruit['name'].isalpha():
                    break
                else:
                    print('과일 이름을 정확하게 입력하세요.')
            check = 0
            for i in fruitlist:
                if i['name'] == fruit['name']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 과일 이름이 있습니다.')
        
        fruit['price'] = int(input('가격 >>> '))

        fruit['cnt'] = int(input('수량 >>> '))
                    
        fruitlist.append(fruit)
        page = len(fruitlist)-1
        print(fruitlist)
   
    if choice=="S": 
        while True:
            print("----------판매항목--------------")
            print(fruitlist)
            choice1 = input('어떤 항목을 판매할까요?')
            choice2=  int(input('몇 개를 판매할까요?'))
            for i in range(len(fruitlist)):
                if fruitlist[i]['name'] == choice1:
                    print(fruitlist[i]['name'], " 항목을 판매합니다.")
                    fruitlist[i]['cnt'] -= choice2
                    SUM += fruitlist[i]['price'] * choice2
                    print("총 판매금액 : ", SUM)
                print("추가적으로 판매하실 항목이 있으십니까?")
                sale_ans= input("Y/N : ").upper()
                if sale_ans == 'Y':
                    choice1 = input('어떤 항목을 판매할까요?')
                    choice2=  int(input('몇 개를 판매할까요?'))
                    for i in range(len(fruitlist)):
                        if fruitlist[i]['name'] == choice1:
                            print(fruitlist[i]['name'], " 항목을 판매합니다.")
                            fruitlist[i]['cnt'] -=choice2
                            SUM += fruitlist[i]['price'] *choice2
                            print("총 판매금액 : ", SUM)
                            print("판매를 종료합니다.")      
                else :
                    print("총 판매금액 : ", SUM)
                    break
            break


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

    elif choice=="B": 
        while True:
            print("----------매입항목--------------")
            print(fruitlist)
            choice1 = input('어떤 항목을 매입할까요?')
            choice2=  int(input('몇 개를 매입할까요?'))
            for i in range(len(fruitlist)):
                if fruitlist[i]['name'] == choice1:
                    print(fruitlist[i]['name'], " 항목을 매입합니다.")
                    fruitlist[i]['cnt'] += choice2
                    SUM += fruitlist[i]['price'] * choice2
                    print("총 매입금액 : ", SUM)
                print("추가적으로 매입하실 항목이 있으십니까?")
                sale_ans= input("Y/N : ").upper()
                if sale_ans == 'Y':
                    choice1 = input('어떤 항목을 매입할까요?')
                    choice2=  int(input('몇 개를 매입할까요?'))
                    for i in range(len(fruitlist)):
                        if fruitlist[i]['name'] == choice1:
                            print(fruitlist[i]['name'], " 항목을 매입합니다.")
                            fruitlist[i]['cnt'] +=choice2
                            SUM += fruitlist[i]['price'] *choice2
                            print("총 매입금액 : ", SUM)
                            print("매입을 종료합니다.")      
                else :
                    print("총 매입금액 : ", SUM)
                    break
            break
            
    elif choice == "Q":
        print('프로그램을 종료합니다.')
        break