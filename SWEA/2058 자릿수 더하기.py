a = input() # 자연수를 str로 받기
b = list(a) # 각 자릿수를 리스트로
total = 0
for i in b: # 리스트의 성분 들을 정수로 바꿔서 더하기 
    total +=  int(i)

print(total)
    
