# 직사각형을 만드는 방법 

'''
https://www.acmicpc.net/problem/8320

변의 길이가 1인 n개의 정사각형으로 만들수 있는 직사각형의 개수는 ? 
회전해서 같으면 같은 직사각형임 

n = 6 일때

1 x 1
1 x 2
1 x 3
1 x 4
1 x 5
1 x 6

2 x 2
2 x 3
'''

def func(n):
    counts = 0
    for i in range(1,n+1):
        for j in range(i,n+1):
            
            if i * j <= n :
                # print((i,j), end=' ')
                counts += 1
            # elif i == j or i > j:
            #     print()
            #     return counts
    return counts

n = int(input())
print(func(n))

