# quiz 01>
# 주민등록번호 14자리를 입력받아서 성별을 체크합니다.
# 프로그램 종료는 (q,Q)를 누를때 까지 반복처리합니다.

# 입력예 : 123456-1234567
# 조건처리 : - 길이값 체크
#           - 성별 체크 (가능값:1,2,3,4)
# 출력 : 여성입니다. or 남성입니다.

# def jumin_check():
#     while True:
#         a = input("주민등록번호 13자리를 입력하세요. '-'도 포함해서 입력\n")
        
#         if len(a) ==14 and (a[7] == '1' or a[7] == '3') and a[6] == '-':
#             print('남성입니다.')
        
#         elif len(a)==14 and (a[7] == '2' or a[7] == '4') and a[6] == '-':
#             print('여성입니다.')
                
#         elif len(a)!=14 and a not in ['q',  'Q']:
#             print('주민등록번호가 14자리가아닌 %d 자리입니다' % len(a))
        
#         elif a == 'q' or a == 'Q':
#             print('종료합니다.')
#             break
            
#         else:
#             print('잘못된 주민등록번호 형식입니다. 다시 입력해주세요.')

# jumin_check()

## 입력 : 주민등록번호
## 리턴값 : 성별

def jumin_check1(a):
        
    if len(a) ==14 and (a[7] == '1' or a[7] == '3') and a[6] == '-':
        gender = '남성'
    
    elif len(a)==14 and (a[7] == '2' or a[7] == '4') and a[6] == '-':
        gender = '여성'
            
    elif len(a)!=14 and a not in ['q',  'Q']:
        gender = '주민등록번호가 14자리가아닌 %d 자리입니다' % len(a)
    
    else:
        print('잘못된 주민등록번호 형식입니다. 다시 입력해주세요.')
    
    return gender

while True:
    a = input("주민등록번호 13자리를 입력하세요. '-'도 포함해서 입력\n")
    if a == 'q' or a == 'Q':
        print('종료합니다.')
        break
    answer=jumin_check1(a)
    print(answer)
