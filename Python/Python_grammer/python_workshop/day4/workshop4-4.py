#2차원 list의 전체 합 구하기 

num_list = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]


def all_list_sum(list):
    list_sum = 0
    for list_index in list:
        for list_index2 in list_index:
            list_sum += list_index2
            
    return list_sum        

print(all_list_sum(num_list))