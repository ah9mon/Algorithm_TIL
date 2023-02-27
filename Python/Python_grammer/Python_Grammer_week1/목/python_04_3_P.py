# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

num_list = list(input()[1:-1].split(', '))
num_list = list(map(int, num_list)) #[1, 1, 3, 3, 0, 1, 1]
# print(num_list)

for index_num in range(len(num_list)-1):
    if num_list[index_num] == num_list[index_num + 1]: # index_num 번째 값과 index_num + 1 값이 같으면
        num_list[index_num + 1] = 'del' # index_num 번쨰 값을 'del' 로 변경

while 'del' in num_list: # num_list에 'del'이 있을 때 까지
    num_list.remove('del') # 'del' 제거



print(num_list)   #[1, 3, 0, 1]     