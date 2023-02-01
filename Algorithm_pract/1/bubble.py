def bubblesort(a,n):
    for i in range(n-1, 0 , -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


n = int(input())
a = list(map(int,input().split())) #[55,7,78,12,42]
bubblesort(a, n)
print(a)