# 순열

def f(i,k,p):
    if i == k :
	    print(p)
    else:
        for j in range(i,k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k, p)

p = [1,2,3]
N = len(p)
f(0, N, p)