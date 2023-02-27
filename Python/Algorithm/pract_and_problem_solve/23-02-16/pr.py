# 순열

def f(i,k,p):

    if i == k :
        print(p)

    else:
        for j in range(i,k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, p)
            p[i], p[j] = p[j], p[i] # 복구

p = [1,2,3]
N = len(p)
f(0, N, p)


# 부분집합

# def f(i,k):
#     if i == k:
#         # print(bit)
#         for index in range(k):
#             if bit[index]:
#                 print(A[index], end = ' ')
#         print('')
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1, k)
#
# A = [1,2,3,4,5]
# N = len(A)
# bit = [0]*N
# f(0,N)
