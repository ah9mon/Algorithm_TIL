def max(list):
    max = list[0]
    for index in list:
        if max < index:
            max = index
    
    return max



def check(list):
    
    count_list = []
    for index_num in range(len(list)):
        count = 0
        for index in list[index_num+1 : ]:
            if list[index_num] > index:
                count += 1

        count_list.append(count)

    return max(count_list) 
    



T = int(input())

for i in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))
    print(f'#{i+1} {check(num_list)}')

