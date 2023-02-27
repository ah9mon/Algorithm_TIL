
def sum_of_digit(num):
    num_list_str = list(str(num))
    num_list_int = list(map(int,num_list_str))
    print(sum(num_list_int))
    return sum(num_list_int)

# def sum_of_digit(num):
#     num_list_str = list(str(num))
#     print(num_list_str)
#     total = 0
#     for index in num_list_str:
#         total += int(index)

#     print(total)
#     return total 

sum_of_digit(3904) # 16
