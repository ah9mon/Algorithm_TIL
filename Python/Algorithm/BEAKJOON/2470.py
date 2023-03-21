# 두용액 

'''
https://www.acmicpc.net/problem/2470
'''

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

min_sum  = 2000000003
start = 0
end = N-1
while start < end :
    s1 = arr[start] + arr[end]
    s2 = abs(s1)
    if s2 < min_sum:
        min_sum = s2
        rlt = [start, end]
    
    if s1 == 0:
        break

    elif s1 > 0:
        end -= 1  

    else:
        start += 1  

# print(min_sum)
print(arr[rlt[0]], arr[rlt[1]])
