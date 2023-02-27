grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

def high_price(grain_list):
    grain_price = []
    for i in range(len(grain_list)): #grain_list의 index 수만큼 반복
        grain_price.append(grain_list[i][1]) # [3000, 2000, 4500, 1300] 

    grain_price.sort() # [1300, 2000, 3000, 4500]

    for i in range(len(grain_list)): #grain_list의 index 수만큼 반복
        if grain_list[i][1] == grain_price[-1]: # 만약 grain_list[i][1] == 4500 이면
            return grain_list[i][0] # 옥수수

print(high_price(grain_lst)) 