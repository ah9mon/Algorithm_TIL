orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = orders.split(',') #['아이스아메리카노', '카라멜마키야또', '에스프레소', '아메리카노', '아메리카노', '아이스라떼', '핫초코', '아이스아메리카노', '아메리카노', '아이스카라멜마키야또', '아이스라떼', '라떼마키야또', '카푸치노', '라떼마키야또']


ice_lst = []
for index1 in orders_list: 
    if '아이스' in index1: #원소에 '아이스가 포함된다면'
        ice_lst.append(index1) #ice_lst에 추가
    else:
        pass     
# print(ice_lst) # ['아이스아메리카노', '아이스라떼', '아이스아메리카노', '아이스카라멜마키야또', '아이스라떼'] 
print(len(ice_lst)) #5 

orders_dict = {}
for index2 in orders_list: 
     if index2 in orders_dict.keys(): #index2가 orders_dict의 키값이라면 
         orders_dict[index2] += 1 #index2의 value값에 +1 
    
     else: #index2가 orders_dict의 키값이 아니라면
         orders_dict[index2] = 1 #orders_dict에 {index2 : 1} 추가


for key1 in orders_dict.keys(): 
     print(key1, orders_dict[key1]) #orders_dict의 키 : 벨류 출력
