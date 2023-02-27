#List의 합 구하기 

def list_sum(num_list):
    num_sum = 0
    
    for num in num_list:
        num_sum += num
    
    return num_sum

print(list_sum([1,2,3,4,5]))    