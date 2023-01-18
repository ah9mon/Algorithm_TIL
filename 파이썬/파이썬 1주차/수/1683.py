blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_dic = {}

for blood in blood_types:
    if blood in blood_dic:
        blood_dic[blood] += 1
    else :
        blood_dic[blood] = 1

print(blood_dic) 