# SWEA D3
'''
분할정복


'''
import sys
sys.stdin = open('input_for_16930.txt')


def q_sort(s,e):
    global counts

    if s == e:
        return
    
    # print(f'{s} ~ {e}')
    
    m = s + (e-s+1)//2 -1
 
    q_sort(s,m)
    q_sort(m+1,e)

    if arr[m] > arr[e]:
        counts += 1 
    # merge()
    k = 0
    l,r = s,m+1 # 왼쪽과 오른쪽에서 가장 작은 수의 위치
    while l <= m or r <= e:
        if l <= m and r <= e: # 왼쪽이랑 오른쪽 비교하면서 tmp에 채우기 
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l<=m : # 왼쪽이 남았을 경우
            while l<=m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r <= e: # 오른쪽이 남았을 경우
            while r <= e:
                tmp[k] = arr[r]
                r += 1
                k += 1
    
    i = 0
    while i<k:
        arr[s+i] = tmp[i]
        i += 1
    return

T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    counts = 0
    tmp = [0] * N
    q_sort(0,N-1)
    print(f'#{i} {arr[N//2]} {counts}')
