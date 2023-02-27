V = int(input())

def pre(n):
    print(n , end=' ')
    pre(child[n][0]) 
    pre(child[n][1]) 

list1 = list(map(int,input().split()))
child = [[] for _ in range(V+2)]
for i in range(len(list1),2):
    child[list1[i]].append(list1[i+1])
    child[list1[i]].sort()

pre(1)

