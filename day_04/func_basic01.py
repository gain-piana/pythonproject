import random, json, time, os

def load_save_data(file,mode,data=None):
    path = os.path.dirname(__file__)+'/'+file
    with open(path,mode) as f:
        if mode == 'r':
            data = json.load(f)
            return data
        elif mode == 'w':
            json.dump(data,f)

def quiz_input(word):
    while True:
        quiz = input('추가할 문제를 입력하세요. >>> ')
        while quiz in word:
            quiz = input('중복된 단어 입니다. 다시 추가할 문제를 입력하세요.(종료 : 0) >>> ')
        if quiz == '0':
            break
        word.append(quiz)
        print(word)
    # load_save_data('word.json','w',word)

def typing_game(word,ranking):
    print('''-------
타자게임
-------''')
    point = 1
    input('시작(enter)')
    start = time.time()
    while point <=1:
        quiz = random.choice(word)
        print(f'\n{point}번' , quiz) # f문자열포맷팅 기억하고 써먹자.
        answer = input('입력하세요 >>> ')
        if quiz == answer:
            print('통과')
            point = point + 1 #point += 1로 하면 더 간단함.
        else:
            print('다시 입력하세요')
    print('\n5문제를 모두 맞추셨습니다. 게임을 종료합니다.')
    end = time.time()
    print(f'걸린시간{end-start:.0f}초')
    name = input('이름을 입력해주세요. >>> ')
    while name in ranking:
        print('사용자명이 중복됩니다.')
        name = input('이름을 입력해주세요. >>> ')
    ranking[name] = end-start
    print(ranking)

def rank_list(ranking):
    print('------ ranking ------')
    ranklist = sorted(ranking.items(),key=lambda x:x[1],)
    for index,(k,v) in enumerate(ranklist):
        print(f'{index+1}등 {k} {v:.2f}')
