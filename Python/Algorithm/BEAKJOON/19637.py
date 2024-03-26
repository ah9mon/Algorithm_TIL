import sys 

def binary_search(p) :
    global N
    start = 0
    end = N - 1

    while (start <= end) :
        mid = (start + end) // 2
        title = titles[mid]
        if (p <= title[1]) :
            end = mid - 1
            
        elif (p > title[1]) :
            start = mid + 1

    print(titles[start][0])

N, M = map(int, sys.stdin.readline().strip().split())
titles = [["", 0] for _ in range(N)]
for i in range(N) :
    title = list(sys.stdin.readline().strip().split())
    title[1] = int(title[1])
    titles[i] = title

titles = sorted(titles, key = lambda x:x[1])

for _ in range(M) :
    power = int(sys.stdin.readline())
    binary_search(power)