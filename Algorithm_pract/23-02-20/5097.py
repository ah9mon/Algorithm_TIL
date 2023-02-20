import sys
sys.stdin = open('input_for_5097.txt')

# from collections import deque
#
# T = int(input())
# for i in range(1,T+1):
#     # 수열의 개수, 작업의 반복 횟수
#     N, M = map(int,input().split())
#
#     # 입력값 큐에 받기
#     q = deque()
#     for num in input().split():
#         q.append(int(num))
#
#     # pop 후 push M번 반복
#     for _ in range(M):
#         q.append(q.popleft())
#
#     print(f'#{i} {q[0]}')

def enqueue():
    global rear
    global q
    if rear+1 >= N: # 큐의 크기 넘어가면
        rear = 0

    else:
        rear += 1

def dequeue():
    global front
    global q
    if front + 1 >= N: #큐의 크기 넘어가면
        front = 0
        return q[front]
    else:
        front += 1
        return q[front]

T = int(input())
for i in range(1,T+1):
    # 수열의 개수, 작업의 반복 횟수
    N, M = map(int,input().split())
    q = list(map(int,input().split()))
    front = 0
    rear = N-1
    for _ in range(M):
        dequeue() # 앞 숫자 빼고
        enqueue() # 뒤에 추가

    print(f'#{i} {q[front]}')


