import sys 
sys.stdin = open('input_for_lawyer.txt')

def strange_lawyer(arr, N):
    counts = 0
    # 가로 확인
    for low1 in range(8):
        for column1 in range(8 - N + 1):
            word_list = arr[low1][column1:column1+N] # 1. N개 묶은 리스트 생성
            # print(f'가로{word_list}')
            if word_list == word_list[::-1]: # 2. 정상과 리버스가 같으면 카운트
                # print(f'가로 카운트')
                counts += 1


    # 세로 확인
    # 1. 각 열의 성분을 담은 리스트를 따로 생성
    for column2 in range(8):
        word_list = []
        for low2 in range(8):
            word_list.append(arr[low2][column2])
        # print(f'세로{word_list}')


        for i in range(8 - N + 1):
            have_to_check = word_list[i:i+N] # 2. 회문 길이 만큼 따로 체크할 리스트 생성
            # print(f'세로 체크{have_to_check}')
            if have_to_check == have_to_check[::-1]: #3. 정상과 리버스 비교
                # print(f'세로 카운트')
                counts += 1

    return counts

# T = int(input())

for i in range(1,11):
    N = int(input())
    board = [list(input()) for j in range(8)]
    print(f'#{i} {strange_lawyer(board,N)}')