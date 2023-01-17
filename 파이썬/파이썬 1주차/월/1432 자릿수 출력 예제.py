s = input('숫자를 입력해주세요 : ')
n_list = list(s) #문자열을 리스트로 n_list = ['1','2','3']
int_n_list = list(map(int, n_list)) #리스트의 원소들을 정수로 변환 
n_sum = sum(int_n_list) # 리스트의 원소들을 모두 sum
print(n_sum) #sum 값을 print