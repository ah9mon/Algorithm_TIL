num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

num_list = [4, 4, 7, 8, 10, 4]
num_list.sort() # [4, 4, 4, 7, 8, 10]

num_dict = {}
for num in num_list:
    if num in num_dict.keys():
        num_dict[num] += 1 
    else : 
        num_dict[num] = 1
        
#print(num_dict) #{4: 3, 7: 1, 8: 1, 10: 1}
#print(num_dict.keys()) #dict_keys([4, 7, 8, 10])

non_one_list = []
for key in num_dict.keys():
    if num_dict[key] != 1:
        non_one_list.append(key)

#print(non_one_list) #[4]
        
for key in non_one_list:
    del(num_dict[key])      
        
        
one_list = num_dict.keys()
#print(one_list) #dict_keys([7, 8, 10])   

sum = sum(one_list)
print(sum) #25


