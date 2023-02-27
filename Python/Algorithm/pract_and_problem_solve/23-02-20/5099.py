# 허리 굽

import sys
sys.stdin = open('input_for_5099.txt')
'''
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다
- > 반복문으로 매번 꺼내서 치즈가 녹은만큼 뺌
- > 한바퀴 돌고와서 녹은양 N / 2 
'''
# from collections import deque
#
# def pizza(M,q):
#     i = N # 현재까지 들어간 피자 번호
#     while len(q) > 1: # 피자가 한판만 남을때 까지
#         # 남은 치즈 확인하려고 꺼냄 : 피자번호, 치즈
#         pizza_num, cheeze = q.popleft()
#         # 꺼낼때는 한바퀴 돈거니까 치즈 반 녹임
#         cheeze = cheeze//2
#         # print(pizza_num,cheeze)
#
#         if cheeze <= 0: # 만약 치즈가 다 녹았으면
#             # 지금 꺼내서 확인한 피자는 그대로 꺼내고 새로운 피자 넣기
#             if i+1 <=  M: # 아직 넣을 피자가 있으면
#                 i += 1
#                 q.append((i, origin_cheeze[i])) # 피자 넣기
#         else: # 만약 치즈가 아직 안녹았으면
#             q.append((pizza_num, cheeze)) # 다시 넣기
#
#     # print(q)
#     return q.popleft()[0]
#
# T = int(input())
# for i in range(1,T+1):
#     # 화덕의 크기 , 피자 개수
#     N, M = map(int,input().split())
#     origin_cheeze = [0] + list(map(int,input().split())) # 피자 번호에 따른 치즈 양
#     push = [0]*(M+1)
#     q = deque() # 화덕
#
#     # 일단 1번부터 N번까지 화덕에 넣기
#     for j in range(1,N+1):
#         # (피자 번호, 치즈양)
#         q.append((j,origin_cheeze[j])) # 화덕에 들어간 피자 치즈
#         push[j] = 1 # 화덕에 넣었다 체크
#
#     # print(q)
#     print(f'#{i} {pizza(M,q)}')



def pizza(M,q):
    i = N # 현재까지 들어간 피자 번호
    while len(q) > 1: # 피자가 한판만 남을때 까지
        # 남은 치즈 확인하려고 꺼냄 : 피자번호, 치즈
        pizza_num, cheeze = q.pop(0)
        # 꺼낼때는 한바퀴 돈거니까 치즈 반 녹임
        cheeze = cheeze//2
        # print(pizza_num,cheeze)

        if cheeze <= 0: # 만약 치즈가 다 녹았으면
            # 지금 꺼내서 확인한 피자는 그대로 꺼내고 새로운 피자 넣기
            if i+1 <=  M: # 아직 넣을 피자가 있으면
                i += 1
                q.append((i, origin_cheeze[i])) # 피자 넣기
        else: # 만약 치즈가 아직 안녹았으면
            q.append((pizza_num, cheeze)) # 다시 넣기

    # print(q)
    return q.pop(0)[0]

T = int(input())
for i in range(1,T+1):
    # 화덕의 크기 , 피자 개수
    N, M = map(int,input().split())
    origin_cheeze = [0] + list(map(int,input().split())) # 피자 번호에 따른 치즈 양
    # push = [0]*(M+1)
    q = [] # 화덕

    # 일단 1번부터 N번까지 화덕에 넣기
    for j in range(1,N+1):
        # (피자 번호, 치즈양)
        q.append((j,origin_cheeze[j])) # 화덕에 들어간 피자 치즈
        # push[j] = 1 # 화덕에 넣었다 체크

    # print(q)
    print(f'#{i} {pizza(M,q)}')




