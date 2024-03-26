import sys

def sumN(n) :
    return (n * (n + 1)) // 2

N = int(sys.stdin.readline())
rlt = - 1
start = 0
end = N
mid = (start + end) // 2

while (start <= end) :
    mid = (start + end) // 2
    s = sumN(mid)
    
    if (s > N) :
        end = mid - 1
    elif (s < N) :
        rlt = mid
        start = mid + 1
    else :
        rlt = mid
        break

print(rlt)