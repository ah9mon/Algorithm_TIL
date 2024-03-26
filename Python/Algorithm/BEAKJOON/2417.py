import sys
import math

N = int(sys.stdin.readline())
start = 0
end = N
mid = - 1
rlt = 0
while(start <= end) :
    mid = (start + end) // 2
    n2 = pow(mid, 2)
    if (n2 < N) :
        start = mid + 1
        rlt = mid + 1
    elif (n2 > N) :
        end = mid - 1
        rlt = mid
    else :
        rlt = mid
        break 

print(rlt)