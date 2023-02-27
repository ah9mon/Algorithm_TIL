# 하루에 4번 사랑을말하고 8번 웃고 6번의 키스를 해줘

import sys
sys.stdin = open('input_for_13801.txt')

def password(N):

    global word

    for i in range(N-1):
        if word[i] == word[i+1]:
            del word[i:i+2]
            break

    if len(word) == N :
        return

    password(len(word))

for i in range(1,11):
    N, word = tuple(input().split())
    N = int(N)
    word = list(map(int,word))
    password(N)
    print(f'#{i} {"".join(str(x) for x in word)}')




