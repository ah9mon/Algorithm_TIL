# 랜선 자르기 

'''
https://www.acmicpc.net/problem/1654

N의 랜선을 만들어야함 

현재는 K개의 랜선을 갖고 있지만 길이가 제가각

K 개의 랜선을 잘라서 모두 같은 길이의 N개의 랜선만들어라 

만들 수 없는 경우는 없다 

항상 길이는 정수 임 

최대 랜선 길이는 ? 

N 너무 큼 -> 이진탐색 
'''

K, N = map(int,input().split())

k_list = [int(input()) for _ in range(K)]
bigone = max(k_list)
start = 1
end = bigone
while start <= end:
    cnt = 0
    center = (start + end) // 2
    for k in k_list:
        cnt += k // center
    if cnt >= N:
        start = center + 1
    else:
        end = center - 1
print(end)
    



