# 백준 동전 바꿔주기 

'''
https://www.acmicpc.net/problem/2624
'''
import copy
# 지폐의 금액
T = int(input())
# 동전의 가지수 
k = int(input())
# 동전의 금액, 개수
arr = [list(map(int,input().split())) for _ in range(k)]
arr.sort(key = lambda x : x[0], reverse = True)
# print(arr)
dp = [0] * (T+1) # 0원 부터 T원 까지
d = [0] * (T+1) # 0원 부터 T원 까지
d[0] += 1
dp[0] += 1

# 10원 부터 내림차순으로 d 채우기 
for i in range(k): 
    # print(f'i : {arr[i][0]}')
    for won in range(T+1): # 0부터  T원 만드는 방법까지 
        if dp[won] > 0: # 그 방법이 1개 이상이면 
            # print(f'현재 원 : {won}')
            for j in range(1,arr[i][1]+1): # 동전 개수 만큼 반복
                sum1 = won + arr[i][0]*j
                # print(f' 현재 합 : {sum1}')
                if sum1 <= T:
                    d[won + arr[i][0]*j] += dp[won] 
    dp = copy.deepcopy(d)
print(dp[T])
# print(d)




