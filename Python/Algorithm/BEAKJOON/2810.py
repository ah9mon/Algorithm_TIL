# 컵 홀더 

N = int(input()) # 사람수

seets = input() # 자리 정보 입력 받기 
counts = 0 # 컵홀더의 개수 
i = 0
# 컵홀더 개수 세기 
while i < N: # 마지막 좌석 확인할 때까지 
    counts += 1 
    if i != N-1 and seets[i] == seets[i+1] == "L": # 만약 커플석의 첫번째이면
        i += 2 # 다다음칸 확인  
    else: # 일반석이면 
        i += 1 # 그냥 다음칸 확인 
counts += 1 # 마지막엔 무조건 컵호더 있으므로 1개 추가 
print(min(counts,N)) # 컵홀더와 사람수 중 작은 수 출력 
        

