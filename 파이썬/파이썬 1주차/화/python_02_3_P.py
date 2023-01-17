str_lst = input('문자열을 입력하세요. : ')

str_lst1 = str_lst.split() # 입력 받은 문자열을 공백 기준으로 나눠서 리스트화

for index_num in range(len(str_lst1) - 1): #str_lst1의 인덱스 수 -1 만큼 반복 
    if casefold(str_lst1[index_num][-1]) != casefold(str_lst1[index_num +1 ][0]): # str_lst1 n번째 원소의 끝 글자와 n+1 번쨰 원소 첫글자가 같지 않으면 
        print('Fail') # fail 출력
        break # 반복문 종료
      
else: ## str_lst1 n번째 원소의 끝 글자와 n+1 번쨰 원소 첫글자가 같지 않은 조건이 나오지 않으면 
    print('pass')    #pass
    

