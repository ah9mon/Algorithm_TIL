def merge_sort(a):
    '''병합정렬'''

    def _merge_sort(a,l,r):
        '''a[l]~a[r]을 재귀적으로 병합 정렬'''
        if l < r:
            c = (l + r) // 2
            _merge_sort(a,l,c)
            _merge_sort(a,c+1,r)
 
            p = j = 0
            i = k = l
            
            # a[l]~a[c]을 buff[0]~buff[c-l+1] 로 복사  
            while i <= c:
                print(f'복사')
                buff[p] = a[i]
                p += 1
                i += 1
            
            # buff가 복사한 부분과 a[c+1:r] 합병해서 arr애 저장  
            while i <= r and j < p:

                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            # buff에 남아 있는 원소를 a에 복사 
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [0] * n
    _merge_sort(a,0,n-1)

    del buff

arr = list(map(int,input().split()))
merge_sort(arr)
print(*arr)