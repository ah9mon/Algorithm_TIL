import sys 

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().strip().split()))
budgets.sort()
max_budget = int(sys.stdin.readline())

start = 0
end = budgets[N - 1]
budget = 0
while (start <= end) :

    mid = (start + end) // 2
    sum_budgets = 0
    for i in range(N):
        if (mid > budgets[i]) :
            sum_budgets += budgets[i]
        else :
            sum_budgets += mid

    if (sum_budgets <= max_budget) :
        start = mid + 1
    elif (sum_budgets > max_budget) :
        end = mid - 1
    
print(end)