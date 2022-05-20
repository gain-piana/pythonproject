# quiz 6>
# 앞에 타자 게임을 활용
# - 1.문제추가 2.타자게임 3.등수리스트 4.종료하기
# - 문제추가 후 데이터는 파일 저장
# - 문제추가는 단어를 입력받아서 중복되지 않게 추가
# - 타자게임은 시간을 체크하고, 걸린시간을 사용자명과 함께 저장합니다. (딕셔너리로 저장)
# - 등수리스트는 걸린시간이 적은 순서대로 정렬해서 출력합니다.
# - 종료하기는 등수데이타를 저장하고 진행합니다.
# - 프로그램이 시작될때 문제와 등수정보를 읽어옵니다.

# word = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'mouse', 'panda', 'frog', 'snake', 'wolf']
# ranking = { '0' : '0' }
# del ranking['0']


import random, json, time
import func_basic01 as fb1

word = fb1.load_save_data('word.json','r')
ranking = fb1.load_save_data('ranking.json','r')

while True:
    choice = input('1.문제추가 2.타자게임 3.등수리스트 4.종료하기 >>> ')
    
    if choice == '1':
        fb1.quiz_input(word)
        fb1.load_save_data('word.json','w'),word
    elif choice == '2':
        fb1.typing_game(word,ranking)
        
    elif choice == '3':
        fb1.rank_list(ranking)
            
    elif choice == '4':
        print('타자게임을 종료합니다.')
        fb1.load_save_data('ranking.json','w',ranking)
        break
    
    else:
        print('1~4까지의 숫자를 입력하세요.\n')    