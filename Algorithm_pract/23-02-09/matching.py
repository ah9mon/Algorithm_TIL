p = 'ab'
t = 'aaaabaaaabaaaab'
M = len(p)
N = len(t)

# def bf(p,t):
#     i = 0
#     j = 0
#     while i < N and j < M:
#         if t[i] != p[j]:
#             i -= j
#             j = -1
#         i += 1
#         j += 1
#     if j == M : return i - M # 검색 성공
#     else: # 검색 실패
#         return 'Fail' 

# print(bf(p,t)) # 3

def bf2(p,t,N,M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        # else: 
        return i

    return 'fail'

print(bf2(p,t,N,M)) 