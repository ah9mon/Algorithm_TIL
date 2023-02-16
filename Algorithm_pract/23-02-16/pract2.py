# 부분집합의 합

# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 구하시오

a = {1,2,3,4,5,6,7,8,9,10}
a = list(a)
N = len(a)

for i in range(1 << N):
    b = [] # 부분집합 리스트
    sum1 = 0
    for j in range(N):
        if i & (1 << j):
            b.append(a[j])
            sum1 += a[j]
            if sum1 > 10: # 합이 10 이상이면 더이상 볼필요가 없으므로 중단
                break
    if sum(b) == 10:
        print(*b)