# 영식이와 친구들

'''
https://www.acmicpc.net/problem/1592

한사람이 공 M번 받으면 끝
공을 받은 횟수가 홀수번이면 -> i + L 에게 공 줌 if i+L > N 이면 i + L - N
공  받   횟    짝       -> i - L 에게 공 줌 if i-L < 1 이면 i - L + N
공을 총 던지는 횟수는 ?
'''

N, M, L = map(int,input().split())

p = [0]*(N+1)
p[1] += 1
i = 1
counts = 0
while not M in p:
    if p[i]%2: # 홀수면
        i += L
        if i > N:
            i -= N
        p[i] += 1
        counts += 1
    else: # 짝수면
        i -= L
        if i < 1:
            i += N
        p[i] += 1
        counts += 1
print(counts)
