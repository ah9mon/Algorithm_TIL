menu = {'pasta' : 10000 , 'burger' : 8000, 'pizza' : 20000}

# print(len(menu))
sum = 0
for dish in menu.keys():
    sum += menu[dish]

print(round(sum / len(menu)))    