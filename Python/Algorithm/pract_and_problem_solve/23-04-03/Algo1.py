
def func():
    '''
    연속 1의 개수를 카운팅 하는 함수
    예를 들어 11110011 이면 12340012가 되고 그 중 가장 큰 수는 연속된 1의 개수 중 최대 값이다

    :return:
    연속된 1의 최대 값 출력
    '''
    a10 = int(a,16) # 주어진 16진수를 10진수로 변환
    a2 = bin(a10) # 10진수를 2진수로 변환
    # print(type(a2)) # str
    a2_lst = list(map(int,a2[2:])) # 2진수 표현 부분만 정수인 리스트로 변환
    # print(a2_lst)
    for i in range(1,len(a2_lst)): # 각 인덱스를 비교하기 위한 반복문
        if a2_lst[i] == 0: # a2_lst[i]가 0 이면
            continue # 넘어가기

        elif a2_lst[i-1] > 0: # a2_lst[i]가 0이 아닌걸 위에서 확인 했으므로 이전 값이 0보다 크면
            a2_lst[i] += a2_lst[i-1] # 이전 값을 현재 값에 더해줌

    print(f'#{tc} {max(a2_lst)}') # 그 중 최대 값이 연속된 1의 최대 개수 이므로 출력

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 16진수의 길이
    a = input() # 16진수 입력
    func()
