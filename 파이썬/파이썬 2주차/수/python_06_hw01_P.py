# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

a = input('1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: (ex.n% mg)')
b = input('2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: (ex.n% mg)')

a_saltwater = a.split()
b_saltwater = b.split()
a_salt_mount = int(a_saltwater[0][0])*int(a_saltwater[1][0]) # 4
#print(a_salt_mount)
b_salt_mount = int(b_saltwater[0][0])*int(b_saltwater[1][0]) # 24
#print(b_salt_mount)
a_water_mount = int(a_saltwater[1][0]) - a_salt_mount
b_water_mount = int(b_saltwater[1][0]) - b_salt_mount

new_water_mount = a_water_mount + b_water_mount
new_salt_mount = a_salt_mount + b_salt_mount
new_saltwater_per =  new_salt_mount / (new_salt_mount + new_water_mount) 
new_saltwater_mount = new_salt_mount + new_water_mount

press_botton = input()
if press_botton == 'Done':
    print(f'{new_saltwater_per}% {new_saltwater_mount}g')
 