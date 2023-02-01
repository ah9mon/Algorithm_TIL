n_m = input().split()

N,M = int(n_m[0]),int(n_m[1])

have_not_listened = set(input() for i in range(N))
have_not_seen = set(input() for i in range(M))

have_not_seen_and_listened = list(have_not_listened & have_not_seen)
have_not_seen_and_listened.sort()
print(len(have_not_seen_and_listened))
for i in have_not_seen_and_listened:
    print(i)

