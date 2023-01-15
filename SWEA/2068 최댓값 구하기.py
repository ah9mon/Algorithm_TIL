a= int(input())

f = [input() for i in range(a)]# 입력

f = list(map(lambda x : x.split() , f )) # 공백 기준으로 리스트



g = []
for i in range(a): 
    g.append(list(map(lambda x : int(x), f[i]))) # g에 f의 인자들을 정수로 바꾸고 리스트화 
    g[i].sort() # g의 인자들을  크기순으로 나열

for i in range(a):
    h = g[i]
    print(f'#{i+1} {h[-1]}')

