#a,b,c,d = int(input()),input(),input(),input()

a= int(input())

f = [input() for i in range(a)]# 입력

f = list(map(lambda x : x.split() , f )) # 공백 기준으로 리스트



g = []
for i in range(a): 
    g.append(list(map(lambda x : int(x), f[i]))) # g에 f의 인자들을 정수로 바꾸고 리스트넣기 
   
        
        

for i in range(a):
    h = g[i] # h에 g[n] 넣기
    total = 0
    for j in range(10):
        total += h[j] # 리스트 h의 인자들을 모두 더함
        average = total / 10 # 평균 구하기 
        
    print(f'#{i+1} {round(average)}') # 평균을 반올림한 것 출력
    


