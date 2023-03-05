# magnetic

'''
1은 n극
2는 s극 
테이블의 크기는 100x100
10개의 테스트 케이스 
'''

import sys
sys.stdin = open("input_for_15701.txt")

def func():
    counts = 0
    arr = list(zip(*magnets))
    for i in range(N):
        line = "".join(arr[i]).replace("0","")
        counts += line.count("12")
    return counts

for i in range(1,11):
    N = int(input())
    magnets = [input().split() for _ in range(N)]
    print(f'#{i} {func()}')
