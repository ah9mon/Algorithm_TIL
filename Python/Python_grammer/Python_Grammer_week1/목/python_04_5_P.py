test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

cheat_list = []
for stnd in  list(test_status.keys()):
	if test_status[stnd] == 'cheating':
		cheat_list.append(stnd)
		del test_status[stnd]

cheat_list.sort()
print(cheat_list)

for stnd in  list(test_status.keys()):
	if test_status[stnd] == 'sleeping':
		test_status[stnd] = 'solving'

print(test_status)