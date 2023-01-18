salt_water_list = []
for i in range(5):
    salt_water = input("소금물의 퍼센트 농도,소금물의양(그만입력 = n) : ")
    if salt_water == 'n':
        break
    salt_water = salt_water.split(',')
    salt_water_list.append(salt_water)

salt_water_sum_switch = input("혼합 하기 (Done 입력) : ")
if salt_water_sum_switch == 'Done':
    print()

print(salt_water_list)
salt_sum = 0
salt_water_sum = 0
for saltwater in salt_water_list:
    salt = (int(saltwater[0])/100)*int(saltwater[1])
    salt_sum += salt
    salt_water_sum += int(saltwater[1])
salt_water_per = salt_sum / salt_water_sum * 100
print(f'혼합물의 퍼센트 농도 : {salt_water_per}')
print(f'혼합물의 양 : {salt_water_sum}')