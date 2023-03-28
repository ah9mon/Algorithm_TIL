###################순열################# 

# def perm(i,k):
#     '''
#     param
#     i : 값을 결정할 인덱스 
#     k : 결정할 개수
#     '''
#     if i == k : 
#         print(*p)
#     else:
#         for j in range(i,k): # 자신부터 오른쪽 원소들과 교환
#             p[i], p[j] = p[j], p[i]
#             perm(i+1,k)
#             p[i], p[j] = p[j], p[i]

# p = [1,2,3]
# perm(0,3)

# def perm(i,k):
#     if i == k:
#         print(*p)
#     else: 
#         for j in range(k): # 첨부터 끝까지 
#             if used[j] == 0: # 사용하지 않은 자리면  
#                 p[i] = A[j]
#                 used[j] = 1 # 사용
#                 perm(i+1, k)
#                 used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게 

# A = [1,2,3]
# p = [0] * 3
# used = [0]*3
# perm(0,3)


##################부분집합################ 
# arr = [3,6,7,1,5,4]
# n = len(arr)

# for i in range(0,(1<<n)): # 부분집합의 개수
#     for j in range(0,n): # 원소의 수만큼 비트 비교
#         if i & (1<<j): # i의 j번째 비트가 1 이면 j번째 원소 출력
#             print(arr[j], end = ' ')
#     print()

#################부분집함 재귀###############
def func(s,e):
    if s == e:
        for i in range(N):
            if bit[i]:
                print(A[i], end = ' ')
        print()
    else:
        bit[s] = 1
        func(s+1,e)
        bit[s] = 0
        func(s+1,e)

A = [7,3,5,3,4]
N = len(A)
bit = [0]*N # bit[i] A[i]원소가 부분집합에 포함되는지 표시함
func(0,N)

#################조합##################
# N = 10 
# for i in range(N):
#     for j in range(i+1,N):
#         for k in range(j+1,N):
#             print(i,j,k)

##############재귀 조합################## 
# def nCr(s,c,e):
#     if c == r:
#         print(*comb)
#         return
#     else:
#         for i in range(s,n):
#             comb[c] = A[i]
#             nCr(i+1,c+1,e)
    
# n = 10
# r = 3
# comb = [0]*3
# A = [i for i in range(n)]
# nCr(0,0,n)

