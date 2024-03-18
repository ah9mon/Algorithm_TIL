import sys
import heapq

hq = []
for _ in range(28) :
    heapq.heappush(hq,int(sys.stdin.readline()))

pre = 0
while(hq) :
    stuNum = heapq.heappop(hq)
    if (stuNum - 1 != pre) :
        print(stuNum - 1)
    
    pre = stuNum

if (pre == 29 and stuNum == 29) :
    print(30)