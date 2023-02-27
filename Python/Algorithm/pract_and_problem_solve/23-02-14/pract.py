# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0 :
#         memo[n] = (fibo1(n-1) + fibo1(n-2))
#
#     return memo[n]
#
# n= 10
# memo = [0] * (n+1) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# memo[0] = 0
# memo[1] = 1
# print(fibo1(3)) # 2


def fibo2(n):
    f = [0]*(n+1)
    f[0], f[1] = 0, 1
    for i in range(2,n+1):
        f[i] = f[i-2] + f[i-1]

    return  f[n]

print(fibo2(3)) # 2