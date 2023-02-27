# A. 입력예시

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(id_num):
    new_id_list = list(id_num) # ['9', '7', '0', '1', '0', '3', '-', '1', '2', '3', '4', '5', '6', '7']
    if '-' in new_id_list:  #new_id_list에 '-'가 있으면
        new_id_list.remove('-') # ['9', '7', '0', '1', '0', '3', '1', '2', '3', '4', '5', '6', '7']
    for i in range(6,13):  # 뒷번호 7자리마다
        new_id_list[i] = '*'  #'*'로 바꿈
    
    return ''.join(new_id_list)



print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))