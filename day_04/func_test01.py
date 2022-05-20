# 파일을 만들때는 이름이 json등 파일과 겹치지 않게 주의해야함.
def test_func(a,b):
    '''
    함수를 작성합니다. #함수 바로 밑에 이런식으로 설명 써놓으면 나중에 함수 호출시에 마우스 갖다대면 여기에 써 놓은 설명이 나옴.
    '''
    print('test_func함수 실행',a,b) #a,b를 매개변수라 부름.

test_func(1,'a') #1, 'a'를 인자값이라 부름.

#syntax error : 문법오류. 따옴표, 괄호등등
#ctrl + F5로 실행하는것과 오른쪽 상단의 세모버튼을 눌러서 실행하는건 차이가있다.
#file-preference-keyboard shortcut에서 단축키 설정 가능

def add1():
    print(1+2)

def add2(a,b):
    print(a+b)

def add(a=1,b=2):
    print(a+b)

add1()
add2(1,4)
add()
add(1,4)
add(b=5,a=3) #b=5가 add중 뒤로, a=3이 add중 앞으로 들어감.

def add4(c,a=1,b=2): #def add4(a=1,b=2,c): 이렇게 쓰면안됨. 디폴트값이 없는 변수는 제일 앞으로 나와야함.
    print(a+b)
    return c+a+b

add4(2)
add4(2,10)

def add5(c,a=1,b=2): 
    print(a+b)
    return c,a,b
x, y, z= add5(2,10)
print(x,y,z)