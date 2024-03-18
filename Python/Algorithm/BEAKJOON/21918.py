import sys

N, M = sys.stdin.readline().split()
lamps = list(map(int, sys.stdin.readline().split()))
for _ in range(int(M)) :
    a,b,c = map(int, sys.stdin.readline().split())
    if (a == 1) :
        lamps[b - 1] = c
    elif (a == 2) :
        for i in range(b - 1,c) :
            if (lamps[i]) :
                lamps[i] = 0
            else :
                lamps[i] = 1
    elif (a == 3) :
        for i in range(b - 1,c) :
            if(lamps[i]) : lamps[i] = 0
        
    elif (a == 4) :
        for i in range(b - 1, c) :
            if (not lamps[i]) : lamps[i] = 1


print(" ".join(map(str, lamps)))