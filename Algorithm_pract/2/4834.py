
# 
# 카드에 들어있는 가장 큰 숫자 만큼 카운트 리스트 생성 
# 

def max_card(cards, n):
    
    # cards의 카드 숫자 리스트 생성 
    card_list = []
    while True:
        card_list.append(cards % 10)
        cards = cards // 10

        if not cards:
            break
    # card_list = [9, 7, 6, 9, 4]
    
    # 숫자 중복 count
    counts = [0] * 10
    for num in card_list:
        counts[num] += 1
    # counts = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # 최댓값 중 가장 큰 인덱스 넘버의 최대값 리턴
    max_count = counts[0] # counts[0] 이 최대값이라 가정
    max_index_num = 0
    for index_num in range(len(counts)):
        if max_count <= counts[index_num]:
            max_count = counts[index_num]
            max_index_num = index_num
    
    return f'{max_index_num} {max_count}'
    
    # # 최댓값들 중 인덱스 넘버가 작은 거 리턴하는 경우 
    # max_count = max(counts)

    # return f'{counts.index(max_count)} {max_count}'

T = int(input())
for i in range(1,T+1):
    N = int(input())
    cards = int(input())
    print(f'#{i} {max_card(cards, N)}')