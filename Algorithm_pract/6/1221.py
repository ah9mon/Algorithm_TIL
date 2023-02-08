# 1
# 딕셔너리 or 튜플 생성 
# 숫자로 변환 후 sort  N + N*logN
# 다시 변환 N



# 2
# 카운트 해서 N
# 정렬 N
import sys
sys.stdin = open("GNS_test_input.txt")

def trans(num_list):
    space_hog = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0] * 10

    # 입력 값에 0~9 각각 몇개씩 있는지 카운트 
    for space_num in num_list:
        earth_num = space_hog.index(space_num)
        counts[earth_num] += 1
    
    # 0~9 까지 순서대로 counts 값만큼 출력
    for i in range(10):
        for _ in range(counts[i]):
            print(space_hog[i], end = ' ')
    print('')

T = int(input())

for i in range(1,T+1):
    tc, N = input().split()
    num_list = input().split()
    N = int(N)
    print(f'#{i}')
    trans(num_list)

