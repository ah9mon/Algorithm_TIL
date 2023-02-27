# 숫자 정렬 

# 카운트 연습 
import sys
sys.stdin = open('input_for_1966.txt')

def count_sort(N,num_list):
    

    A = num_list # 입력 배열 
    B = [0]*N # 정렬된 배열 
    C = [0]*(max(A) + 1) # 카운트 배열
    # print(A)

    for i in A:
        C[i] += 1
    
    # print(C)

    for j in range(1,len(C)):
        C[j] += C[j-1]
    
    # print(C)

    for k in range(N-1,-1,-1):
        C[A[k]] -= 1
        B[C[A[k]]] = A[k]

    # print(B)
    b = list(map(str,B))
    return ' '.join(b)

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    print(f'#{i} {count_sort(N,num_list)}')
