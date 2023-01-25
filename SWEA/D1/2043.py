try1 = 0 
a = input()
P, K = tuple(a.split())
print(P,K)
for i in range(int(K),int(P)+1):
    try1 += 1
print(try1)