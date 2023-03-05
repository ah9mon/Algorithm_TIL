# 의석이의 세로로 말해요 

import sys
sys.stdin = open('input_for_13684.txt')

'''
단어들은 모두 받은뒤에 try except로 처리 
'''
def func():
    # 문자열의 길이 1~15
    for index in range(15):
        # 모든 단어들의 index 번째 문자 출력 
        for word in words:
            try: 
                print(word[index],end='')
            except: # out of index 무시 
                continue

T = int(input())
for i in range(1,T+1):
    # 단어들을 입력받아 리스트에 넣기 
    words = [] 
    for _ in range(5):
        words.append(input())
    print(f'#{i}',end=' ')
    func()
    print()