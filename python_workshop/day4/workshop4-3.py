#dictionary로 이루어진 List의 합 구하기

mans = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]


   

def dict_list_sum(list):
    age_sum = 0
    for index in list:
        age_sum += index['age']
        
    return age_sum
    
print(dict_list_sum(mans))    