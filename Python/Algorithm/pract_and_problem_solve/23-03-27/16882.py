# SWEA babygin

'''
3장의 카드가 연속적인 번호를 갖는 경우 run 
3장의 카드가 동일한 번호를 갖는 경우 triplet
6장의 카드가 run과 triplet으로만 이루어진 경우 baby-gin
'''
import sys
sys.stdin = open('input_for_16882.txt')

T = int(input())
for _ in range(T):
    cards = input()
    d = [0]*10
    for card in cards:
        d[int(card)] += 1

    triplets = 0
    run = 0
    for i in range(8):
        if d[i] and d[i+1] and d[i+2]: # 연속 3개가 1이상이면 
            while d[i] and d[i+1] and d[i+2]: # 연속 3개가 1이상일 때까지
                triplets += 1
                d[i] -= 1
                d[i+1] -= 1
                d[i+2] -= 1
        
        if d[i] >= 3: # 3장 이상 같은 카드 있을 경우
            while d[i]:
                run += 1
                d[i] -= 3


    if (run + triplets) >= 2:
        print('True')
    else:
        print('False')


    
