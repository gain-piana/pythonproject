def fruit_input(fruitlist):
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
    
    while True:
        fruitprice = input('가격 >>> ')
        if fruitprice.isnumeric():
            break
    fruit['price'] = int(fruitprice)

    while True:
        fruitcnt = input('수량 >>> ')
        if fruitcnt.isnumeric():
            break
    fruit['cnt'] = int(fruitcnt)
                
    fruitlist.append(fruit)
    print("----------판매항목--------------")
    for i in range(len(fruitlist)):
        print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))
    print("--------------------------------")   

def fruit_s(fruitlist,SUM):

        while True:
            print("----------판매항목--------------")
            print(fruitlist)
            choice1 = input('어떤 항목을 판매할까요? >>>')
            choice2=  int(input('몇 개를 판매할까요? >>>'))
            
            while choice2 > 0: 
                for i in fruitlist:
                    if i['name'] == choice1:
                        if choice2 >=0 and choice2 <= i['cnt']:
                            print('good')
                        
                        else:
                            print('판매할 수 있는 최대 수량은',i['cnt'],'입니다')
                            print('다시 입력해주세요 ')
                            choice2=  int(input('몇 개를 판매할까요? >>>'))

                break
                        
               

            for i in range(len(fruitlist)):
                if fruitlist[i]['name'] == choice1:
                    print(fruitlist[i]['name'], " 항목을 판매합니다. >>>")
                    fruitlist[i]['cnt'] -= choice2
                    SUM += fruitlist[i]['price'] * choice2
                    print("총 판매금액 : ", SUM)

            while True:
                print("추가적으로 판매하실 항목이 있으십니까? >>>")
                sale_ans= input("Y/N : ").upper()
                if sale_ans == 'Y':
                    choice1 = input('어떤 항목을 판매할까요? >>>')
                    choice2=  int(input('몇 개를 판매할까요? >>>'))
                    for i in range(len(fruitlist)):
                        if fruitlist[i]['name'] == choice1:
                            print(fruitlist[i]['name'], " 항목을 판매합니다.")
                            fruitlist[i]['cnt'] -=choice2
                            SUM += fruitlist[i]['price'] *choice2
                            print("총 판매금액 : ", SUM)
    

                else :
                    print("총 판매금액 : ", SUM)
                    break
            break
        return SUM
def fruit_c(fruitlist):
        print("재고 리스트 출력합니다.")
        print("-------------------------")
        for i in range(len(fruitlist)):
            print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))

        print("-------------------------")   
        
def fruit_d(fruitlist):
    print("----------판매항목--------------")
    for i in range(len(fruitlist)):
        print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))

    print("--------------------------------")
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
    print("----------판매항목--------------")
    for i in range(len(fruitlist)):
        print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))

    print("--------------------------------")