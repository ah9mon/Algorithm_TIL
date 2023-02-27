N = int(input())

arr = list(map(int,input().split()))

rlt = []
for i in range(N):
    rlt.insert(i - arr[i], i+1)
    print(rlt)

print(*rlt)
    