import sys

sys.stdin = open('input_for_pract2.txt')

def sum_of_part(list1):
    N = len(list1)
    counts = 0

    for i in range(1 , 1<<N):
        part = []
        for j in range(N):
            if i & (1<<j):
                part.append(list1[j])
        
        if sum(part) == 0:
            print(f'{part} of sum is 0')
            counts +=1

    return 1 if counts > 0 else 0


T = int(input())

for i in range(1,T+1):
    num_list = list(map(int, input().split()))
    print(num_list)
    print(f'#{i} {sum_of_part(num_list)}')