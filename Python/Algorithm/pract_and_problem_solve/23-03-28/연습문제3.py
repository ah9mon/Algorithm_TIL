def func(s,e):
    if s == e:
        if sum(rlt) == 0:
            for num in rlt:
                if num:
                    print(num, end=' ')
            print()
    else:
        rlt[s] = arr[s]
        func(s+1,e)
        rlt[s] = 0
        func(s+1,e)    

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(arr)
rlt = [0]*n
func(0,n)
