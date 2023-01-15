a,b = int(input()), input()

b = b.split() # 공백을 기준으로 문자열 나누고 리스트로
c = []
for i in b[1:]:
    c.append(int(i)) # 리스트 성분을 정수로

c.sort() # 리스트를 크기순으로 정렬
    

index_num = int((a-1)/2) # 중간값의 인덱스 넘버 계산
print(c[index_num]) # 중간값 출력

