a = int(input()) # 정수 입력

for i in range(1,a+1): 
    if a % i == 0: # 나머지가 0 이면 (약수이면)
        print(i, end =' ') # 출력
