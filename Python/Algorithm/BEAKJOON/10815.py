import sys

def binary_search(n) :
    start = 0
    end = N - 1
    mid = -1
    while(start <= end) :
        mid = (start + end) // 2
        if (n < cards[mid]) :
            end = mid - 1
        elif (n > cards[mid]) :
            start = mid + 1
        else :
            return 1
    
    return 0

    
    

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().strip().split()))
cards.sort()

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M) :
    if (i == M - 1) :
        print(binary_search(nums[i]))
    else :
        print(binary_search(nums[i]), end = " ")