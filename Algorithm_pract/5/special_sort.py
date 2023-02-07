import sys
sys.stdin = open('sample_input (2).txt')

# T = int(input())

# for i in range(1,T+1):
#     N = int(input())
#     num_list = list(map(int,input().split()))
    
#     num_list = sorted(num_list)
#     num_list_reverse = sorted(num_list, reverse = True)
#     new_list = []
#     for j in range(5):
#         new_list.append(num_list_reverse[j])
#         new_list.append(num_list[j])
    
#     print(f'#{i} {" ".join(str(x) for x in new_list)}')

T = int(input())

for i in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    
    num_list = sorted(num_list)
 
    new_list = []
    for j in range(5):
        new_list.append(num_list[-(j+1)])
        new_list.append(num_list[j])
    
    print(f'#{i} {" ".join(str(x) for x in new_list)}')

    