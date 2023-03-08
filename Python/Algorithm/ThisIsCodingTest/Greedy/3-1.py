'''
거스름돈

N 원 주어지고 
동전이 500원 , 100원, 50원, 10원짜리가 무한히 있을때
거슬러 줘야 할 동전의 최소 개수는 ?
'''

N = int(input()) # 항상 10의 배수
coins = [500,100,50,10]
rlt = 0
# while N > 0:
#     if N >= 500: # 500원 이상이면 
#         rlt += N // 500
#         N %= 500
#     elif N >= 100:
#         rlt += N // 100
#         N %= 100
#     elif N >= 50:
#         rlt += N // 50
#         N %= 50
#     elif N >= 10:
#         rlt += N // 10
#         N %= 10

for coin in coins:
    rlt += N // coin
    N %= coin

print(rlt)




