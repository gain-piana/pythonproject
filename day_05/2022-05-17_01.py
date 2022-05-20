fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 5},
          {'name': '포도', 'price': 4000, 'cnt': 20},
          {'name': '수박', 'price': 10000, 'cnt': 5} ]

import function_fruitlist as ff
SUM=0
while True:
    choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        C - 재고리스트
        D - 삭제
        Q - 종료
        ''').upper()

    if choice=="I":
        ff.fruit_input(fruitlist)

    elif choice=="S": 
        SUM= ff.fruit_s(fruitlist,SUM)

    elif choice == 'C':
        ff.fruit_c(fruitlist)     

    elif choice == 'D':
        ff.fruit_d(fruitlist)

    elif choice == "Q":
        print('프로그램을 종료합니다.')
        break