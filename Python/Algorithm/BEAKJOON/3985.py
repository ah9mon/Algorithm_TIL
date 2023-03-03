# 롤 케이크 

'''
https://www.acmicpc.net/problem/3985

'''

L = int(input()) # 롤케이크 길이 
N = int(input()) # 방청객의 수 

cake = [0] * (L+1)
expect = 0 # 가장 많은 조각을 받을 것으로 기대되번 방청객의 번호
expect_max = 0 # 그의 예상 조각수

for human in range(1,N+1): # 방청객 
    P,K = map(int,input().split()) # 방청객이 선택한 케이크 P~K

    if K-P+1 > expect_max: # 현재 방청객의 예상 케이크 수보다 최대 예상 케이스수가 크다면 
        expect_max = K-P+1 # 케이크 수 할당
        expect = human # 방청객 번호 할당 

    for num in range(P,K+1): # 하나하나 확인 
        if not cake[num]: # 선택한 사람이 없으면 (0이면)
            cake[num] = human # 그 방청객의 케이크가 됨

# 방청객이 가져간 케이크 개수 카운트 
humans = [0]*(N+1) 
for piece in cake:
    humans[piece] += 1

print(expect) # 예상 케이크가 가장 많은 방청객 
print(humans[1:].index(max(humans[1:])) + 1) # 실제로 가져간 케이크가 가장 많은 방청객 

