import sys 

N = int(sys.stdin.readline())
cows = [-1 for _ in range(N + 1)]
count = 0
for _ in range(N) :
    cow = list(map(int, sys.stdin.readline().split()))
    if (cows[cow[0]] < 0) :
        cows[cow[0]] = cow[1]
    else:
        if (cows[cow[0]] == 0 and cow[1] == 1) :
            count += 1
            cows[cow[0]] = cow[1]
        elif (cows[cow[0]] == 1 and cow[1] == 0) :
            count += 1
            cows[cow[0]] = cow[1]

print(count)